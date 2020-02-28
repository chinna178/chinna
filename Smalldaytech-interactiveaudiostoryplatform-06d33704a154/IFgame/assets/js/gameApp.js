


  $('#recButton').on('click',function(e){
    document.getElementById("song").pause();
  e.preventDefault();
    document.getElementById("story").pause();

    document.getElementById("song").volume = 0.2;


 //alert('start');
 $.ajax({
    url: '//127.0.0.1:8000/gameApp/start',
    type: 'get', // This is the default though, you don't actually need to always mention it
    success: function(data) {
      //  alert('s_start');
          document.getElementById("story").play();
          document.getElementById("song").play();
          $('#recButton').removeClass("Rec");
          $('#recButton').addClass("notRec");

    },
    failure: function(data) {
        console.log('Got an error dude');
    }
});
});






$('#end').on('click',function(e){
  e.preventDefault();
 document.getElementById("story").pause();
 document.getElementById("story").currentTime=0;
   document.getElementById("song").play();
    document.getElementById("song").currentTime=0;
      document.getElementById("song").volume = 0.2;
});
