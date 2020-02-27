$(document).ready(function() {

    $('#refresh').click(function() {
        location.reload();
    });

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $('#submit_button').click(function(event) {
        event.preventDefault();
        let form_val = $('form p input').val();
        let data_to_server = {
            "form_value": form_val
        };
        $.ajax({
            type: "GET",
            url: "/",
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            scriptCharset: "utf-8",
            data: data_to_server,
            success: function(resp, textStatus, xhr) {
                if (xhr.status === 200) {
                    console.log(resp);
                    display_url(resp)

                }
            },
            error: function(data) {
                alert("Sorry, smth goes wrong");
            }
        });
    });
});

function display_url(resp) {
    let new_url = `<div class="text-center" id= class="short_url">
<p>Feel free to use this one:</p>
                        <h2><a href="${resp['cut_url_ready']}">${resp['cut_url_ready']}</a></h2>
                       </div>`;
    $('#wrapper').prepend(new_url).fadeTo();
    $('form').fadeOut()
};