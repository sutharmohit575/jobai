function toggleNav() {
    document.querySelector('.nav-links').classList.toggle('open');
}

// Auto-dismiss messages after 4s
document.querySelectorAll('.message').forEach(m => {
    setTimeout(() => m.remove(), 4000);
});

// Animate score rings on resume detail page
document.querySelectorAll('[data-score]').forEach(el => {
    const score = parseFloat(el.dataset.score);
    const circumference = 2 * Math.PI * 54;
    const offset = circumference - (score / 100) * circumference;
    const fill = el.querySelector('.score-ring-fill');
    if (fill) {
        fill.style.strokeDasharray = circumference;
        fill.style.strokeDashoffset = circumference;
        setTimeout(() => { fill.style.strokeDashoffset = offset; }, 200);
    }
});

// Animate stat numbers
document.querySelectorAll('.stat-num[data-target]').forEach(el => {
    const target = parseInt(el.dataset.target);
    let current = 0;
    const step = Math.ceil(target / 40);
    const timer = setInterval(() => {
        current = Math.min(current + step, target);
        el.textContent = current.toLocaleString() + (el.dataset.suffix || '');
        if (current >= target) clearInterval(timer);
    }, 30);
});

// File upload preview
const fileInput = document.querySelector('input[type="file"]');
if (fileInput) {
    fileInput.addEventListener('change', function() {
        const zone = document.querySelector('.upload-zone');
        if (zone && this.files[0]) {
            zone.querySelector('.upload-title').textContent = this.files[0].name;
            zone.querySelector('.upload-sub').textContent = 
                (this.files[0].size / 1024).toFixed(1) + ' KB · Ready to upload';
            zone.style.borderColor = 'var(--accent)';
            zone.style.background = 'rgba(0,255,178,0.04)';
        }
    });
}
