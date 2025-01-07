let initial = 0; 

let slides = document.getElementsByClassName("slide"); 
console.log(slides)

let images = ["static/screen1.png","/static/screen2.png"];

// let images = [
//      "{{url_for('static', filename = 'screen1.png') }}",
//          "{{url_for('static', filename = 'screen2.png')}}" ];

function manSide()
{
    let side = document.getElementById("side");
    side.classList.toggle('active'); 


}

let ham = document.querySelector('.ham');
ham.addEventListener('click', manSide)
function slide()
{
    console.log("SLide called. ")
    for(let i = 0; i < slides.length; i++)
        {
            slides[i].classList.remove("show");
            slides[i].style.opacity = 0;
        }

    slides[initial].style.backgroundImage = `url(${images[initial]})`;

    slides[initial].classList.add("show");  // Apply the transition class

    slides[initial].style.opacity = 1; 

}

function change(num)
{
    initial += num; 
    
    if (initial >= slides.length)
        {
            initial = 0; 
        }  
    else if (initial < 0) {
        initial = slides.length - 1;  // Go back to the last slide if initial is negative
    }
    slide(); 
}

slide(); 

setInterval(() => {change(1); }, 5000);

