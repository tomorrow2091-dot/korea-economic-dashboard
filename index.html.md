<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2025년 실시간 글로벌 경제 대시보드 | Global Investment Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* 기존 스타일 유지 */
    </style>
</head>
<body>
    <div class="header">
        <h1>● 2025년 실시간 글로벌 경제 대시보드</h1>
        <p id="lastUpdateTime">마지막 업데이트: ...</p>
        <!-- 기타 대시보드 콘텐츠 -->
        <button id="github-connect" class="github-btn">
            <span>
                <span style="font-size: 1.3em; margin-right: 8px;">🔗</span>
                Connect to GitHub Repository
            </span>
        </button>
    </div>
    <!-- 대시보드 본문 -->
    <p id="giciScore"></p>
    <p id="bitcoinUsd"></p>
    <p id="bitcoinKrw"></p>

    <!-- 실시간 데이터 fetch 스크립트 -->
    <script>
    document.getElementById('github-connect').onclick = function() {
        window.open('https://github.com/tomorrow2091-dot/korea-economic-dashboard', '_blank');
    };

    fetch('./data/dashboard_data.json')
      .then(response => response.json())
      .then(function(data) {
        document.getElementById('lastUpdateTime').textContent = '마지막 업데이트: ' + data.last_updated_display;
        document.getElementById('giciScore').textContent = 'GICI: ' + data.gici.current_score;
        document.getElementById('bitcoinUsd').textContent = 'BTC/USD: ' + data.crypto.bitcoin.usd.toLocaleString();
        document.getElementById('bitcoinKrw').textContent = 'BTC/KRW: ' + data.crypto.bitcoin.krw.toLocaleString();
      });
    </script>
</body>
</html>