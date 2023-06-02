const sidebarTags = document.getElementsByClassName('sidebar_tag');
for (let i = 0; i < sidebarTags.length; i++) {
  sidebarTags[i].addEventListener('click', function() {
    const sidebarJS = this.nextElementSibling;
    sidebarJS.style.display = sidebarJS.style.display === 'block' ? 'none' : 'block';
  });
}

  