// add csrf token to ajax posts
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start, c_end));
        }
    }
    return "";
}
$(function () {
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        }
    });
});

$(document).ready(function () {
    // add click function to upvote buttons
    $('div.vote-buttons button.vote-up').click(function () {
            var id = $(this).attr("id").split("-")[2];
            var vote_type = 'up';
            if ($(this).hasClass('selected')) {
                // remove upvote
                $.post('/vote', {
                    id: id,
                    type: vote_type
                }, function (response) {
                    if (response["status"] == "200") {
                        $("#vote-up-" + id).removeClass('selected');
                        var currentVotes = Number($("#totalvotes-" + id)[0].innerHTML)
                        $("#totalvotes-" + id)[0].innerHTML = currentVotes - 1
                    }
                });
            } else {
                // add upvote
                $.post('/vote', {
                    id: id,
                    type: vote_type
                }, function (response) {
                    if (response["status"] == "200") {
                        $("#vote-up-" + id).addClass('selected');
                        var currentVotes = Number($("#totalvotes-" + id)[0].innerHTML)
                        $("#totalvotes-" + id)[0].innerHTML = currentVotes + 1
                        if ($("#vote-down-" + id).hasClass("selected")) {
                            $("#totalvotes-" + id)[0].innerHTML = currentVotes +
                                2
                        }
                        $("#vote-down-" + id).removeClass("selected")
                    }
                });
            }
        }),
        // add click function to downvote buttons
        $('div.vote-buttons button.vote-down').click(function () {
            var id = $(this).attr("id").split("-")[2];
            var vote_type = 'down';
            if ($(this).hasClass('selected')) {
                // remove downvote
                $.post('/vote', {
                    id: id,
                    type: vote_type
                }, function (response) {
                    if (response["status"] == "200") {
                        $("#vote-down-" + id).removeClass('selected');
                        var currentVotes = Number($("#totalvotes-" + id)[0].innerHTML)
                        $("#totalvotes-" + id)[0].innerHTML = currentVotes + 1
                        $("#vote-up-" + id).removeClass("selected")
                    }
                });
            } else {
                // add downvote
                $.post('/vote', {
                    id: id,
                    type: vote_type
                }, function (response) {
                    if (response["status"] == "200") {
                        $("#vote-down-" + id).addClass('selected');
                        var currentVotes = Number($("#totalvotes-" + id)[0].innerHTML)
                        $("#totalvotes-" + id)[0].innerHTML = currentVotes - 1
                        if ($("#vote-up-" + id).hasClass("selected")) {
                            $("#totalvotes-" + id)[0].innerHTML = currentVotes -
                                2
                        }

                        $("#vote-up-" + id).removeClass("selected")
                    }
                });
            }
        }),
        // add click function to delete buttons
        $('div.modify-buttons p button.topic-delete').click(function () {
            var id = $(this).attr("id").split("-")[1];
            $.post("/topic-delete", {
                id: id
            }, function(response) {
                if (response["status"] == 200) {
                    $("#" + id + "-container").remove();
                }
            })
        })
    });

// i wonder what this will do
function wellcum() {
    $("#audio")[0].play();
  }
