const sidebarTags = document.getElementsByClassName('sidebar_tag');
for (let i = 0; i < sidebarTags.length; i++) {
    sidebarTags[i].addEventListener('click', function() {
        const sidebarJS = this.nextElementSibling;
        if (sidebarJS.style.display === 'block') {
            sidebarJS.style.display = 'none';
        } else {
            sidebarJS.style.display = 'block';
        }
    });
}

const sidebarTagones = document.getElementsByClassName('sidebar_tag_one');
for (let i = 0; i < sidebarTagones.length; i++) {
    sidebarTagones[i].addEventListener('click', function() {
        const sidebarJS = this.nextElementSibling;
        if (sidebarJS.style.display === 'block') {
            sidebarJS.style.display = 'none';
        } else {
            sidebarJS.style.display = 'block';
        }
    });
}

const countElement = document.getElementById("count");
const countValue = parseInt("{{ view.count }}");
countElement.textContent = countValue.toLocaleString();