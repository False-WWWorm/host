<script>
let time = document.querySelector(".time");      // Берём аудио дорожку
let btnPlay = document.querySelector(".play");   // Берём кнопку проигрывания
let btnPrev = document.querySelector(".prev");   // Берём кнопку переключения предыдущего трека
let btnNext = document.querySelector(".next");   // Берём кнопку переключение следующего трека
let playlist = [
    {% for i in pl %}
        "{{i}}",
    {% endfor %}
];

let treck; // Переменная с индексом трека

// Событие перед загрузкой страницы
window.onload = function() {
    treck = 0; // Присваиваем переменной ноль
}

function lib (exp){
    audio.src = './static/audio/' + exp.innerHTML;
    treck = playlist.indexOf(exp.innerHTML);
}

function switchTreck (numTreck) {
    // Меняем значение атрибута src
    audio.src = './static/audio/' + playlist[numTreck];
    play();
}

function play (){
			btnPlay.innerHTML = "❚ ❚";
            //$('.control').addClass('ppause')
            //$('.control').removeClass('pplay')
			audio.play();
            let name_track = playlist[treck];
            document.getElementById("name").innerHTML = name_track;
    // Запуск интервала
    audioPlay = setInterval(function() {
        let audioTime = Math.round(audio.currentTime);
        let audioLength = Math.round(audio.duration)
        // Назначаем ширину элементу time
        time.style.width = (audioTime * 100) / audioLength + '%';
        //блок длительности трека
        let seconds = String(audioTime%60);
        let len = String(audioLength%60);
        document.getElementById('11').innerHTML = parseInt(audioTime/60) + ":" + seconds.padStart(2, '0') ;
        document.getElementById('songlen').innerHTML = parseInt(audioLength/60) + ":" + len.padStart(2, '0') ;
        // Свап при окончании
        if (audioTime == audioLength && treck < (playlist.length-1)) {
            treck++;
            switchTreck(treck);
        } else if (audioTime == audioLength && treck >= (playlist.length-1)) {
            treck = 0;
            switchTreck(treck);
        }
    }, 10)
}

btnPlay.onclick = function (){
    if (btnPlay.innerHTML == "▶"){
play()
    }else{
        btnPlay.innerHTML = "▶";
    audio.pause();
    clearInterval(audioPlay);
    }

}
    //перемотка
      var audio = document.getElementsByTagName('audio')[0];
      var progressBar = document.getElementsByTagName('progress')[0];
      if(audio && progressBar){
    progressBar.addEventListener('click', function(event){
      var x = event.pageX - this.offsetLeft;
      var clickedValue = x * this.max / this.offsetWidth;
      //progressBar.value = clickedValue;
      audio.currentTime = audio.duration * (clickedValue / 100);
      progressBar.value = 0;
    });
      }


btnPrev.addEventListener("click", function() {
    progressBar.value = 0;
    btnPlay.innerHTML = "❚ ❚";
    if (treck > 0) {
        treck--;
        switchTreck(treck);
    } else {
        treck = playlist.length-1;
        switchTreck(treck);
    }
});

btnNext.addEventListener("click", function() {
    progressBar.value = 0;
    btnPlay.innerHTML = "❚ ❚";
    if (treck < (playlist.length-1)) {
        treck++;
        switchTreck(treck);
    } else {
        treck = 0;
        switchTreck(treck);
    }
});

var slider = document.getElementById("volumebar");
slider.oninput = function (){
    audio.volume = this.value / 100;
}

$('.control').on('click', function() {
    $(this).addClass('ppause');
    $(this).removeClass('pplay');
});
</script>