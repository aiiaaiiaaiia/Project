var inputlang = '';

fetch('/vdo_info', {
    method: 'GET',
    dataType: 'json'
})
.then(r => r.json())
.then(data => {
    nameofvideo = data.file_name
    document.getElementById("file_name").innerHTML = nameofvideo;
    console.log(data.file_name)
    console.log(inputlang)
    console.log(tranlang)
    if (data.file_name != 'None'){
        document.getElementById('submitBtn').disabled = false;
    }
    }
);
function submit(){
    if(chinese_value){
        inputlang = inputlang.concat('Chinese ');
    }
    if(german_value){
        inputlang = inputlang.concat('German ');
    }
    if(english_value){
        inputlang = inputlang.concat('English ');
    }
    if(french_value){
        inputlang = inputlang.concat('French ');
    }
    if(italian_value){
        inputlang = inputlang.concat('Italian ');
    }
    if(japanese_value){
        inputlang = inputlang.concat('Japanese ');
    }
    if(korean_value){
        inputlang = inputlang.concat('Korean ');
    }
    if(spanish_value){
        inputlang = inputlang.concat('Spanish ');
    }
    if(thai_value){
        inputlang = inputlang.concat('Thai ');
    }
    if(inputlang == ''){
        inputlang = 'Auto detect the language (Default)'
    }
    if(tranlang == false){ //(Default)
        tranlang = 'English'
    }
    console.log(inputlang)
    document.getElementById("from_lang").innerHTML = inputlang;
    document.getElementById("tran_to_lang").innerHTML = tranlang;

    $.post( "/vdo_uploaded", {
        js_inputlang: inputlang,
        js_tranlang: tranlang
    });

    document.getElementById("button_autodetect").disabled = true;
    document.getElementById("button_chinese").disabled = true;
    document.getElementById("button_german").disabled = true;
    document.getElementById("button_english").disabled = true;
    document.getElementById("button_french").disabled = true;
    document.getElementById("button_italian").disabled = true;
    document.getElementById("button_japanese").disabled = true;
    document.getElementById("button_korean").disabled = true;
    document.getElementById("button_spanish").disabled = true;
    document.getElementById("button_thai").disabled = true; 
    document.getElementById("submitBtn").disabled = true; 
    document.getElementById("button_upload").disabled = true;
    document.getElementById("tran_to_thai").disabled = true;
    document.getElementById("tran_to_english").disabled = true;

    // languages = {
    //     'from': inputlang,
    //     'to': tranlang
    // }
}

                              