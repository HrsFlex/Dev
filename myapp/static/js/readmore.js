
    document.getElementById('readMoreButton').onclick = function() {
        const moreText = document.getElementById('moreText');
        if (moreText.style.display === 'none') {
            moreText.style.display = 'block';
            this.innerText = 'Read Less';
        } else {
            moreText.style.display = 'none';
            this.innerText = 'Read More';
        }
    };

