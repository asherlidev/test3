<template>
    <header id="header">
  <div class="ant-row">
    <div
      class="ant-col-xs-24 ant-col-sm-24 ant-col-md-6 ant-col-lg-5 ant-col-xl-5 ant-col-xxl-4"
    >
      <a href="/vue-antd" class="router-link-active" id="logo"
        ><img
          alt="logo"
          height="32"
          src="//q-fe.aixuexi.com/arch-head/img/header/new-logo.png"
      /></a>
    </div>
    <div
      class="ant-col-xs-0 ant-col-sm-0 ant-col-md-18 ant-col-lg-19 ant-col-xl-19 ant-col-xxl-20"
    >
      <div id="search-box" style="display: block;">
        <i class="anticon anticon-search"></i>
        <div
          class="ant-select ant-select-enabled ant-select ant-select-enabled"
          style="width: 200px;"
        >
          <div
            role="combobox"
            aria-autocomplete="list"
            aria-haspopup="true"
            aria-expanded="false"
            tabindex="0"
            class="ant-select-selection ant-select-selection--single"
          >
            <div class="ant-select-selection__rendered">
             
              <div
                class="ant-select-search ant-select-search--inline"
                style="display: none;"
              >
                <div class="ant-select-search__field__wrap">
                  <input
                    autocomplete="off"
                    value=""
                    class="ant-select-search__field"
                  /><span class="ant-select-search__field__mirror">&nbsp;</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
     
    </div>
  </div>
</header>

</template>
<style>  
  #header {
      transition: all .3s;
      background: #fff;
      box-shadow: 0 2px 8px #f0f1f2;
      position: relative;
      z-index: 10;
      max-width: 100%;
      
  }
</style>
<script>
 export default {
    name:"HeaderBar",
    data(){

    }
 }
</script>