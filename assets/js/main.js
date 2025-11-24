document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.createElement('div');
    overlay.className = 'image-zoom-overlay';
    document.body.appendChild(overlay);

    const zoomedImage = document.createElement('img');
    overlay.appendChild(zoomedImage);

    const galleryImages = document.querySelectorAll('.gallery img');

    galleryImages.forEach(img => {
        img.addEventListener('click', () => {
            zoomedImage.src = img.src;
            overlay.classList.add('show');
        });
    });

    overlay.addEventListener('click', () => {
        overlay.classList.remove('show');
    });
});
