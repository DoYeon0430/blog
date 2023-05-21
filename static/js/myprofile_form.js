    // Get the current URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const tag = urlParams.get('tag');

    // Add the "a" class to the corresponding <a> tag
    if (tag === '대표글') {
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
