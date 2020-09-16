<template>
  <div>
    <h3>캡쳐카메라</h3>
    <input id="myFileInput camera1" @change="change1" type="file" accept="image/*;capture=camera" >

    <h3>캡처카메라 2번째 버전</h3>
    <input @change="change2"  type="file" accept="image/*" capture="camera" id="camera2">

    <h3>이미지 업로드 버전</h3>
    <input  @change="change3"  id="file camera3" type="file" accept="image/*">

    <h3>Mozilla Multiple</h3>
    <input  @change="change4" type="file" id="file camera4" name="file" multiple>

    <img id="frame1">
    <img id="frame2">
    <img id="frame3">
    <div id="frame4">
    </div>
  </div>
</template>

<script>
// var camera1 = document.getElementById('camera1');
// var camera2 = document.getElementById('camera2');
// var camera3 = document.getElementById('camera3');
// var camera4 = document.getElementById('camera4');

// var frame1 = document.getElementById('frame1');
// var frame2 = document.getElementById('frame2');
// var frame3 = document.getElementById('frame3');
// var frame4 = document.getElementById('frame4');


export default {
  name: 'DiaryCreate',
  methods: {
    change1(e) {
      var file = e.target.files[0];
      var frame1 = document.getElementById('frame1');
      frame1.src = URL.createObjectURL(file)
    },
    change2(e) {
      var file = e.target.files[0];
      var frame2 = document.getElementById('frame2');
      frame2.src = URL.createObjectURL(file)
    },
    change3(e) {
      var file = e.target.files[0];
      var frame3 = document.getElementById('frame3');
      frame3.src = URL.createObjectURL(file)
    },
    change4(e) {
      var files = e.target.files
      var frame4 = document.getElementById('frame4');
      for (var file of files) {
        console.log(file)
        var i = document.createElement("img")
        i.src = URL.createObjectURL(file)
        frame4.appendChild(i)
      }
    },
  }
}



// camera2.addEventListener('change', function(e) {
//   var file = e.target.files[0];
//   frame2.src = URL.createObjectURL(file)
// })
// camera3.addEventListener('change', function(e) {
//   var file = e.target.files[0];
//   frame3.src = URL.createObjectURL(file)
// })
// camera4.addEventListener('change', function(e) {
//   var file = e.target.files[0];
//   frame4.src = URL.createObjectURL(file)
// })

</script>

<style>

</style>