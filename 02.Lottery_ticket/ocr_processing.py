# ocr_processing.py
import re


def parse_ocr_result(text):
    # 각 행에 대한 금액과 횟수를 추출
    pattern = re.compile(r"(\d{1,3}(?:,\d{3})*)(?:P)\s*(\d+)")
    matches = pattern.findall(text)
    data = []
    for amount_str, count_str in matches:
        # 쉼표를 제거하고 정수로 변환
        amount = int(amount_str.replace(",", ""))
        count = int(count_str)
        data.append({"amount": amount, "count": count})
    return data


def process_data(data):
    # 횟수에 따라 데이터 정렬
    data_sorted_by_count = sorted(data, key=lambda x: x["count"], reverse=True)

    # 최대 및 최소 금액 추출
    max_transaction = data_sorted_by_count[0]
    min_transaction = data_sorted_by_count[-1]

    # 총 금액과 평균 횟수 계산
    total_amount = sum(d["amount"] * d["count"] for d in data)
    average_count = sum(d["count"] for d in data) / len(data)

    # 결과 반환
    return {
        "max_amount": max_transaction["amount"],
        "max_count": max_transaction["count"],
        "min_amount": min_transaction["amount"],
        "min_count": min_transaction["count"],
        "total_amount": total_amount,
        "average_count": average_count,
    }
