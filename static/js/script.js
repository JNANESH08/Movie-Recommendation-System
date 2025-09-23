function myFunction(obj)
{
  if(obj.value=="Hindi")
  {
    document.getElementById("img1").src="static/imgs/my_background_hindi_1.jpg";
    console.log("hindi");
  }
  else if(obj.value=="English")
  {
    document.getElementById("img1").src="static/imgs/my_background_1.jpg";
    document.title="Netflix india best TV shows and films"
    console.log("english");
  }
}
window.addEventListener('resize',myfunc())
function myfunc()
{
    console.log(window.innerHeight);
    console.log(window.innerWidth);
}
