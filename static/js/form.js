document.addEventListener('DOMContentLoaded', function() {
    const deleteLinks = document.querySelectorAll('.delete-comment');
    deleteLinks.forEach(function(link, index) {
      link.addEventListener('click', function(event) {
        event.preventDefault();
        const deleteForms = document.querySelectorAll('.delete-form');
        deleteForms.forEach(function(form, formIndex) {
          if (formIndex === index) {
            form.style.display = form.style.display === 'none' ? 'flex' : 'none';
          } else {
            form.style.display = 'none';
          }
        });
      });
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    var expandLink = document.getElementById('expand-link');
    var closeLink = document.getElementById('close-link');
    var commentForm = document.getElementById('comment-form');
  
    expandLink.addEventListener('click', function(event) {
      event.preventDefault();
      expandLink.style.display = 'none';
      closeLink.style.display = 'inline-block';
      commentForm.style.display = 'block';
    });
  
    closeLink.addEventListener('click', function(event) {
      event.preventDefault();
      closeLink.style.display = 'none';
      expandLink.style.display = 'inline-block';
      commentForm.style.display = 'none';
    });
  });