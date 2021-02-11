from allauth.socialaccount.models import SocialAccount
from django.db.models import Count
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Topic
from .forms import AddTopicForm, EditTopicForm, DeleteTopicForm


def index(request):
    uncompleted_topics = Topic.objects.filter(completed=False).annotate(votes=(Count(
        "users_upvoted", distinct=True) - Count("users_downvoted", distinct=True))).order_by("-votes")
    completed_topics = Topic.objects.filter(completed=True).annotate(votes=(Count(
        "users_upvoted", distinct=True) - Count("users_downvoted", distinct=True))).order_by("-votes")

    context = {
        "uncompleted_topics": uncompleted_topics,
        "completed_topics": completed_topics
    }

    if request.user.is_authenticated:
        # get up/downvoted posts for user
        context["user_upvotes"] = [i["id"] for i in Topic.objects.filter(
            users_upvoted=request.user.id).values("id")]
        context["user_downvotes"] = [i["id"] for i in Topic.objects.filter(
            users_downvoted=request.user.id).values("id")]

        # get login provider for user
        user_provider = SocialAccount.objects.filter(
            user=request.user.id).get()

        if user_provider.provider == "discord":
            context["display_user_name"] = user_provider.extra_data["username"] + \
                "#" + user_provider.extra_data["discriminator"]
        elif user_provider.provider == "github":
            context["display_user_name"] = user_provider.extra_data["login"]

    return render(request, "index.html", context)


def vote(request):
    if request.user.is_authenticated:
        if request.POST:
            topic_id = int(request.POST.get("id"))
            vote_type = request.POST.get("type")

            this_topic = get_object_or_404(Topic, pk=topic_id)
            if this_topic.completed:
                return JsonResponse({"status": 403, "msg": "votes for completed topics not allowed"})

            thisUserUpVote = this_topic.users_upvoted.filter(
                id=request.user.id).count()
            thisUserDownVote = this_topic.users_downvoted.filter(
                id=request.user.id).count()

            if thisUserUpVote == 0 and thisUserDownVote == 0:
                if vote_type == "up":
                    this_topic.users_upvoted.add(request.user)
                    return JsonResponse({"status": 200, "msg": "voted up"})
                elif vote_type == "down":
                    this_topic.users_downvoted.add(request.user)
                    return JsonResponse({"status": 200, "msg": "voted down"})
                else:
                    return JsonResponse({"status": 400, "msg": "vote_type must be up or down"})
            elif thisUserUpVote == 0 and thisUserDownVote == 1:
                if vote_type == "up":
                    this_topic.users_upvoted.add(request.user)
                    this_topic.users_downvoted.remove(request.user)
                    return JsonResponse({"status": 200, "msg": "changed downvote to upvote"})
                elif vote_type == "down":
                    this_topic.users_downvoted.remove(request.user)
                    return JsonResponse({"status": 200, "msg": "removed downvote"})
                else:
                    return JsonResponse({"status": 400, "msg": "vote_type must be up or down"})
            elif thisUserUpVote == 1 and thisUserDownVote == 0:
                if vote_type == "up":
                    this_topic.users_upvoted.remove(request.user)
                    return JsonResponse({"status": 200, "msg": "removed upvote"})
                elif vote_type == "down":
                    this_topic.users_upvoted.remove(request.user)
                    this_topic.users_downvoted.add(request.user)
                    return JsonResponse({"status": 200, "msg": "changed upvote to downvote"})
                else:
                    return JsonResponse({"status": 400, "msg": "vote_type must be up or down"})
            else:
                return JsonResponse({"status": 500, "msg": "something went wrong on the server"})

        return JsonResponse({"status": 405, "msg": "only post requests allowed"})

    return JsonResponse({"status": 401, "msg": "you need to authorize to vote"})


def topic_new(request):
    if request.user.is_authenticated:
        if request.POST:
            form = AddTopicForm(request.POST)
            if form.is_valid():
                this_topic = form.cleaned_data["topic_input"]
                if not this_topic:
                    return HttpResponseRedirect('/')
                topic_new = Topic.objects.create(
                    title=this_topic, user_created=request.user)
                topic_new.users_upvoted.add(request.user)
    return HttpResponseRedirect('/')


def topic_edit(request):
    if request.user.is_authenticated:
        if request.POST:
            form = EditTopicForm(request.POST)
            if form.is_valid():
                this_topic = form.cleaned_data["topic_input"]
                topic_id = form.cleaned_data["topic_id"]
                if not this_topic:
                    return HttpResponseRedirect('/')
                Topic.objects.update_or_create(id=topic_id, defaults={
                    "title": this_topic
                })

    return HttpResponseRedirect('/')


def topic_delete(request):
    if request.user.is_authenticated:
        if request.POST:
            form = DeleteTopicForm(request.POST)
            if form.is_valid():
                topic_id = form.cleaned_data["topic_id"]
                if not topic_id:
                    return HttpResponseRedirect('/')
                Topic.objects.get(id=topic_id).delete()

    return HttpResponseRedirect('/')
