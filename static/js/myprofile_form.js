    // Get the current URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const tag = urlParams.get('tag');
    // Add the "a" class to the corresponding <a> tag
    if (tag === '영화') {
        const a1 = document.getElementById('a1');
        const a2 = document.getElementById('a2');
        a1.classList.add('myprofile_main_div_js_1');
        a2.classList.add('myprofile_main_div_js_2');
        
    } else if (tag === '프로그래밍') {
        const a1 = document.getElementById('a1');
        const a2 = document.getElementById('a2');
        a1.classList.add('myprofile_main_div_js_2');
        a2.classList.add('myprofile_main_div_js_1');
    }

    const myprofileFormDiv = document.getElementById('myprofileFormDiv');
    const scrollButtongo = document.getElementById('scrollButtongo');
    const scrollButtonback = document.getElementById('scrollButtonback');

    scrollButtongo.addEventListener('click', () => {
      let leftValue;
    
      if (window.innerWidth >= 1400) {
        leftValue = 1314;
      } else if (window.innerWidth >= 1200 && window.innerWidth <= 1399.98) {
        leftValue = 1134;
      } else if (window.innerWidth >= 992 && window.innerWidth <= 1199.98) {
        leftValue = 954;
      } else if (window.innerWidth >= 768 && window.innerWidth <= 991.98) {
        leftValue = 720;
      } else if (window.innerWidth >= 576 && window.innerWidth <= 767.98) {
        leftValue = 540;
      } else {
        // 575.98px 이하일 경우 전체 너비로 설정
        leftValue = window.innerWidth;
      }
    
      myprofileFormDiv.scrollBy({
        top: 0,
        left: leftValue,
        behavior: 'smooth'
      });
    });
    
    scrollButtonback.addEventListener('click', () => {
      let leftValue;
    
      if (window.innerWidth >= 1400) {
        leftValue = -1314;
      } else if (window.innerWidth >= 1200 && window.innerWidth <= 1399.98) {
        leftValue = -1134;
      } else if (window.innerWidth >= 992 && window.innerWidth <= 1199.98) {
        leftValue = -954;
      } else if (window.innerWidth >= 768 && window.innerWidth <= 991.98) {
        leftValue = -720;
      } else if (window.innerWidth >= 576 && window.innerWidth <= 767.98) {
        leftValue = -540;
      } else {
        // 575.98px 이하일 경우 전체 너비로 설정
        leftValue = -window.innerWidth;
      }
    
      myprofileFormDiv.scrollBy({
        top: 0,
        left: leftValue,
        behavior: 'smooth'
      });
    });
    
    