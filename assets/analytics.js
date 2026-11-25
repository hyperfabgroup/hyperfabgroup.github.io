(function () {
  const measurementId = 'G-JN41LMM2VL';

  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }

  gtag('js', new Date());
  gtag('config', measurementId, {
    allow_google_signals: false,
    allow_ad_personalization_signals: false,
  });

  const googleTag = document.createElement('script');
  googleTag.async = true;
  googleTag.src = 'https://www.googletagmanager.com/gtag/js?id=' + measurementId;
  document.head.append(googleTag);

  function trackOrderSiteClick(event) {
    const link = event.target.closest('a[href]');
    if (!link || event.defaultPrevented) return;
    if (link.protocol !== 'https:' && link.protocol !== 'http:') return;
    if (link.hostname !== 'hyperfab.ir' && link.hostname !== 'www.hyperfab.ir') return;

    gtag('event', 'order_site_click', { link_domain: link.hostname });
  }

  document.addEventListener('click', trackOrderSiteClick);
  document.addEventListener('auxclick', function (event) {
    if (event.button === 1) trackOrderSiteClick(event);
  });
})();
