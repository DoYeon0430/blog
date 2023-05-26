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

