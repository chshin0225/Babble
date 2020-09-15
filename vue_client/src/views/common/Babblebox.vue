<template>
  <div class="">
    <div class="scallop-down"></div>
    <div class="text-center">
      <h3 class="color-pink font-weight-bold">Babble Box</h3>
      <p>현재 <span class="color-blue font-weight-bold">아롱이맘</span>님께서 예뻐해주시는 아기입니다.</p>
    </div>
    <!-- <div class="scallop-down"></div> -->
    <div class="babbleboxes w-75 mt-3">
      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>아롱이</p>
            <p>D + 73</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>

      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>샛별이</p>
            <p>D + 120</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>

      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>초롱이</p>
            <p>D + 32</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>

      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>재롱이</p>
            <p>D + 244</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>

      <div class="babblebox d-flex justify-content-between my-3">
        <div class="babblebox-info d-flex">
          <div class="profile mr-3">
            <img src="http://bit.do/babbleprofile">
          </div>
          <div class="babble-box">
            <p>다롱이</p>
            <p>D + 160</p>
          </div>
        </div>
        <div class="babblebox-enter d-flex align-items-center pointer">
          <i class="fas fa-sign-in-alt"></i>
        </div>
      </div>
    </div>
    <div style="height: 100px"></div>

  </div>
</template>

<script>
export default {
  name: 'Babblebox',
}
</script>

<style scoped>

p {
  margin: 0;
}

.profile img {
  max-width: 50px;
  height: auto;
  border-radius: 50%;
}

.babbleboxes {
  margin-left: auto;
  margin-right: auto;
}

.babblebox {
  border: 1px solid #FEA59C;
  border-radius: 50px;
  padding: 10px 30px 10px 30px;
}

.scallop-down{
  height:40px;
  /* margin-left: auto;
  margin-right: auto; */
  width:100%;
  background: -webkit-gradient(radial, 50% 0, 18, 50% 0, 31, from(#9BC7FF), color-stop(0.49, #9BC7FF), color-stop(0.51, #fff), to(white));
  -webkit-background-size: 49px 100%;
}

</style>