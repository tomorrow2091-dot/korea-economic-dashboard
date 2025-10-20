import requests
import json

# 기존 데이터 소스 URL 혹은 API 엔드포인트
COUNTRIES_URL = 'https://api.example.com/countries'
INDICES_URL = 'https://api.example.com/indices'
STOCK_THEMES_URL = 'https://api.example.com/stock-themes'
CRYPTO_URL = 'https://api.coinmarketcap.com/v1/ticker/'
REAL_ESTATE_URL = 'https://api.example.com/real-estate'
GICI_URL = 'https://api.example.com/gici'

# 데이터 수집 함수들

def fetch_json(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def main():
    # 국가별 데이터
    countries = fetch_json(COUNTRIES_URL) or []

    # 경제 지표 (indices)
    indices = fetch_json(INDICES_URL) or {}

    # 글로벌 주식 테마
    stock_themes = fetch_json(STOCK_THEMES_URL) or []

    # 암호화폐 데이터 (예: 비트코인, 이더리움)
    crypto_list = fetch_json(CRYPTO_URL) or []
    crypto = {item['id']: {'usd': float(item['price_usd']), 'krw': float(item.get('price_krw', 0))}
              for item in crypto_list}

    # 부동산 데이터
    real_estate = fetch_json(REAL_ESTATE_URL) or {}

    # GICI 지수
    gici = fetch_json(GICI_URL) or {}

    # 최종 JSON 조합
    dashboard_data = {
        "version": "2.0",
        "last_updated": None,
        "last_updated_display": None,
        "year": 2025,
        "data_source": "GitHub 실시간 연동",
        "countries": countries,
        "indices": indices,
        "stock_themes": stock_themes,
        "crypto": crypto,
        "real_estate": real_estate,
        "gici": gici
    }

    # 타임스탬프 및 표시용 날짜 추가
    from datetime import datetime
    now = datetime.now()
    dashboard_data['last_updated'] = now.isoformat()
    dashboard_data['last_updated_display'] = now.strftime('%Y년 %m월 %d일 %H:%M KST')

    # JSON 파일로 저장
    with open('data/dashboard_data.json', 'w', encoding='utf-8') as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=2)

    print('Dashboard data updated successfully.')

if __name__ == '__main__':
    main()