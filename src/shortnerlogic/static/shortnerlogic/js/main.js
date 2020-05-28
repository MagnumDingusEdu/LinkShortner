// window.onload = play();

var intervalID = window.setInterval(play, 1500);


function play() {
    title = document.getElementById("mainheadingtext");
    title.innerHTML = "Ln-K";
    index = 0;
    while (index < 3) {

        setTimeout(() => { title.innerHTML += "." }, (index + 1) * 500);
        index++;
        // if (index == 3) {
        //     index = 0;
        //     
        // }

    }


}