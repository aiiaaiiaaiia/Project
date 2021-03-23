var inputlang = '';

fetch('/vdo_info', {
    method: 'GET',
    dataType: 'json'
})
.then(r => r.json())
.then(data => {
    var vdo_name = document.getElementById("title");
    var trans_lang = document.getElementById("tran_to_lang");
    var from_lang = document.getElementById("from_lang");
    var text_position = document.getElementById("text_position");
    vdo_name.innerHTML = data.title;
    trans_lang.innerHTML = data.trans_language;
    from_lang.innerHTML = data.language;
    text_position.innerHTML = data.position;
    if (data.title != 'None'){
        document.getElementById('submitBtn').disabled = false;
    };
    }
);
