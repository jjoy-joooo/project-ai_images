# main.py
from ocr_processing import parse_ocr_result, process_data

# OCR로부터 추출된 텍스트
extracted_text = """
1,000P 4
3,000P 3
5,000P 2
"""

# 추출된 텍스트 파싱
data = parse_ocr_result(extracted_text)

# 데이터 처리
results = process_data(data)

# 결과 출력
print(
    f"최대 금액 (가장 높은 횟수): {results['max_amount']}원 ({results['max_count']}회)"
)
print(
    f"최소 금액 (가장 낮은 횟수): {results['min_amount']}원 ({results['min_count']}회)"
)
print(f"총 금액: {results['total_amount']}원")
print(f"평균 횟수: {results['average_count']:.2f}회")
