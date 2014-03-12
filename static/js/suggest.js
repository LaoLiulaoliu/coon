$(document).ready(function() {

    var countDown = function(secs, jurl) {
        document.getElementById('jump').innerText = secs;
        if (--secs > 0)
            setTimeout(
                function() { countDown(secs, jurl); },
                1000);
        else
            location.href = jurl;
    }

    $('#suggestion form.suggest').submit(function(event) {
        $.post('/suggest.html',
            {
                opinion: $('#suggestion form textarea.contractus').val(),
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
            },
            function(data, status) {
                if (data.status === 1) {
                    $('#suggestion .suggest').hide();
                    $('#suggestion .jump').show();
                    $('#suggestion .jump').css({'font-size': '140%', 'text-align': 'center'});
                    countDown(5, '/');
                }
        });
    });
});

