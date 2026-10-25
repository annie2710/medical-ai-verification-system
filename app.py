import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Medical AI Verification System",
    page_icon="🩺",
    layout="wide",
)

TEXT = {
    "English": {
        "title": "Medical AI Verification System",
        "subtitle": "A decision-support prototype for reviewing AI-generated health information against trusted sources.",
        "language": "Interface language",
        "notice_title": "Important medical and legal disclaimer",
        "notice": "This tool is a research prototype, not a medical device and not a substitute for professional medical advice, diagnosis, or treatment. It does not automatically establish whether a medical claim is true. In an emergency, contact local emergency services. Always consult a qualified healthcare professional before making health decisions.",
        "ack": "I have read and understood this disclaimer.",
        "start": "Continue",
        "input_title": "1. AI-generated health information",
        "input_help": "Paste the answer or medical claim you want to review.",
        "input_label": "AI-generated answer / claim",
        "claim_label": "Specific claim being assessed (optional)",
        "source_title": "2. Check trusted sources",
        "source_text": "Search official sources, then review the actual page and its date. Search links do not mean that the claim has been verified.",
        "who": "Search WHO",
        "cdc": "Search CDC",
        "nih": "Search NIH / MedlinePlus",
        "source_name": "Source name",
        "source_url": "Source URL",
        "source_date": "Publication or update date (if available)",
        "evidence_label": "Summarize the relevant evidence from the source",
        "evidence_help": "Paste a short summary in your own words, or a short relevant excerpt. Do not paste sensitive personal medical information.",
        "assessment_title": "3. Evidence assessment",
        "assessment_help": "Select a status only after reviewing relevant evidence. This is a human-assisted assessment, not an automatic fact-check.",
        "supported": "Supported by the reviewed evidence",
        "contradicted": "Contradicted by the reviewed evidence",
        "mixed": "Evidence is mixed or context-dependent",
        "insufficient": "Insufficient evidence / not assessed",
        "status": "Evidence status",
        "green": "GREEN — The reviewed source appears to support the claim. This is not a guarantee of safety or correctness.",
        "red": "RED — The reviewed source appears to contradict the claim. Avoid relying on the claim without professional review.",
        "yellow_mixed": "YELLOW — Evidence is mixed or context-dependent. Further expert review is recommended.",
        "yellow_insufficient": "YELLOW — Evidence is insufficient or has not been assessed. Do not interpret this as proof that the claim is safe.",
        "review_title": "4. Reviewer quality assessment",
        "review_help": "This prototype uses an adapted set of quality-review questions inspired by DISCERN and JAMA benchmarks. It is not the complete validated DISCERN instrument, and the score must not be interpreted as medical accuracy.",
        "reviewer": "Reviewer role",
        "reviewer_options": ["Healthcare professional / expert", "Researcher", "Student", "Other / not specified"],
        "discern_title": "DISCERN-informed quality questions",
        "discern_items": [
            "Are the aims clear?",
            "Is the information relevant to the stated aims?",
            "Are the sources of information identified?",
            "Is the date of the information clear?",
            "Is uncertainty or lack of evidence acknowledged?",
            "Is more than one plausible explanation or option considered?",
            "Are benefits and risks explained where relevant?",
            "Does the information encourage consultation with a qualified professional?",
        ],
        "jama_title": "JAMA benchmark checks",
        "jama_items": ["Authorship / responsible organization is identified", "Attribution / references are provided", "Disclosure of conflicts of interest is available", "Currency / dates for relevant content are available"],
        "yes": "Yes / present",
        "no": "No / absent",
        "unknown": "Unclear / not applicable",
        "result_title": "5. Review summary",
        "score": "Quality-review score",
        "score_note": "Adapted score: 8 questions × 1–5 points. This is a structured reviewer rating, not a validated clinical risk score.",
        "jama_score": "JAMA benchmark checks present",
        "claim": "Claim reviewed",
        "evidence": "Evidence summary",
        "source": "Reviewed source",
        "status_label": "Evidence status",
        "reviewer_label": "Reviewer role",
        "disclaimer_end_title": "Final disclaimer",
        "disclaimer_end": "This result reflects the information and reviewer selections entered into this prototype. It is not an automated or definitive medical fact-check and does not guarantee that a claim is safe, accurate, complete, or applicable to an individual. Sources may be incomplete or outdated. Consult a qualified healthcare professional for personal medical decisions.",
        "download": "Download review summary (.txt)",
        "empty": "Enter a claim or AI-generated answer above to prepare a review.",
        "missing": "Please acknowledge the disclaimer before continuing.",
        "rate_help": "Choose a rating from 1 (very poor) to 5 (excellent). Choose 3 if uncertain.",
    },
    "Tiếng Việt": {
        "title": "Hệ thống xác minh thông tin y tế do AI tạo sinh cung cấp",
        "subtitle": "Bản mẫu hỗ trợ rà soát thông tin sức khỏe do AI tạo sinh cung cấp dựa trên nguồn đáng tin cậy.",
        "language": "Ngôn ngữ giao diện",
        "notice_title": "Tuyên bố miễn trừ trách nhiệm y tế và pháp lý quan trọng",
        "notice": "Đây là bản mẫu nghiên cứu, không phải thiết bị y tế và không thay thế tư vấn, chẩn đoán hoặc điều trị của chuyên gia y tế. Công cụ không tự động xác định một tuyên bố y khoa là đúng hay sai. Trong trường hợp khẩn cấp, hãy liên hệ dịch vụ cấp cứu tại địa phương. Luôn tham khảo chuyên gia y tế đủ năng lực trước khi quyết định liên quan đến sức khỏe.",
        "ack": "Tôi đã đọc và hiểu tuyên bố miễn trừ trách nhiệm này.",
        "start": "Tiếp tục",
        "input_title": "1. Thông tin sức khỏe do AI tạo sinh cung cấp",
        "input_help": "Dán câu trả lời hoặc tuyên bố y tế bạn muốn rà soát.",
        "input_label": "Câu trả lời / tuyên bố do AI tạo ra",
        "claim_label": "Tuyên bố cụ thể cần đánh giá (không bắt buộc)",
        "source_title": "2. Kiểm tra nguồn đáng tin cậy",
        "source_text": "Tìm nguồn chính thức, sau đó tự đọc trang và kiểm tra ngày đăng. Đường dẫn tìm kiếm không có nghĩa là tuyên bố đã được xác minh.",
        "who": "Tìm trên WHO",
        "cdc": "Tìm trên CDC",
        "nih": "Tìm trên NIH / MedlinePlus",
        "source_name": "Tên nguồn",
        "source_url": "URL nguồn",
        "source_date": "Ngày xuất bản hoặc cập nhật (nếu có)",
        "evidence_label": "Tóm tắt bằng chứng liên quan từ nguồn",
        "evidence_help": "Tóm tắt bằng lời của bạn hoặc dán một đoạn ngắn liên quan. Không dán thông tin y tế cá nhân nhạy cảm.",
        "assessment_title": "3. Đánh giá bằng chứng",
        "assessment_help": "Chỉ chọn trạng thái sau khi đã xem xét bằng chứng phù hợp. Đây là đánh giá có con người hỗ trợ, không phải kiểm chứng tự động.",
        "supported": "Được bằng chứng đã xem xét hỗ trợ",
        "contradicted": "Bị bằng chứng đã xem xét phản bác",
        "mixed": "Bằng chứng trái chiều hoặc phụ thuộc bối cảnh",
        "insufficient": "Chưa đủ bằng chứng / chưa đánh giá",
        "status": "Trạng thái bằng chứng",
        "green": "XANH LÁ — Nguồn đã xem xét có vẻ hỗ trợ tuyên bố. Điều này không đảm bảo an toàn hoặc chính xác tuyệt đối.",
        "red": "ĐỎ — Nguồn đã xem xét có vẻ phản bác tuyên bố. Không nên dựa vào tuyên bố này nếu chưa có chuyên gia xem xét.",
        "yellow_mixed": "VÀNG — Bằng chứng trái chiều hoặc phụ thuộc bối cảnh. Nên được chuyên gia đánh giá thêm.",
        "yellow_insufficient": "VÀNG — Bằng chứng chưa đủ hoặc chưa được đánh giá. Không được hiểu điều này là bằng chứng cho thấy tuyên bố an toàn.",
        "review_title": "4. Đánh giá chất lượng bởi người rà soát",
        "review_help": "Bản mẫu sử dụng bộ câu hỏi điều chỉnh lấy cảm hứng từ DISCERN và các tiêu chí JAMA. Đây không phải toàn bộ công cụ DISCERN đã được thẩm định; điểm số không thể hiện độ chính xác y khoa.",
        "reviewer": "Vai trò người đánh giá",
        "reviewer_options": ["Chuyên gia / nhân viên y tế", "Nhà nghiên cứu", "Sinh viên", "Khác / chưa xác định"],
        "discern_title": "Câu hỏi chất lượng tham khảo DISCERN",
        "discern_items": [
            "Mục tiêu có rõ ràng không?",
            "Thông tin có liên quan đến mục tiêu đã nêu không?",
            "Nguồn thông tin có được xác định không?",
            "Ngày của thông tin có rõ ràng không?",
            "Sự không chắc chắn hoặc thiếu bằng chứng có được thừa nhận không?",
            "Có xem xét nhiều cách giải thích hoặc lựa chọn hợp lý không?",
            "Lợi ích và rủi ro có được giải thích khi phù hợp không?",
            "Thông tin có khuyến khích tham khảo chuyên gia y tế đủ năng lực không?",
        ],
        "jama_title": "Kiểm tra các tiêu chí JAMA",
        "jama_items": ["Có xác định tác giả / tổ chức chịu trách nhiệm", "Có ghi nguồn / tài liệu tham khảo", "Có công bố xung đột lợi ích", "Có ngày tháng cho nội dung liên quan"],
        "yes": "Có / hiện diện",
        "no": "Không / vắng mặt",
        "unknown": "Không rõ / không áp dụng",
        "result_title": "5. Tóm tắt đánh giá",
        "score": "Điểm rà soát chất lượng",
        "score_note": "Điểm điều chỉnh: 8 câu hỏi × 1–5 điểm. Đây là đánh giá có cấu trúc của người rà soát, không phải thang điểm nguy cơ lâm sàng đã được thẩm định.",
        "jama_score": "Số tiêu chí JAMA hiện diện",
        "claim": "Tuyên bố được rà soát",
        "evidence": "Tóm tắt bằng chứng",
        "source": "Nguồn đã xem xét",
        "status_label": "Trạng thái bằng chứng",
        "reviewer_label": "Vai trò người đánh giá",
        "disclaimer_end_title": "Tuyên bố miễn trừ trách nhiệm cuối cùng",
        "disclaimer_end": "Kết quả phản ánh thông tin và lựa chọn đánh giá được nhập vào bản mẫu này. Đây không phải kiểm chứng y khoa tự động hoặc mang tính kết luận, và không đảm bảo tuyên bố an toàn, chính xác, đầy đủ hay phù hợp với một cá nhân. Nguồn có thể thiếu hoặc lỗi thời. Hãy tham khảo chuyên gia y tế đủ năng lực trước khi quyết định về sức khỏe cá nhân.",
        "download": "Tải tóm tắt đánh giá (.txt)",
        "empty": "Nhập tuyên bố hoặc câu trả lời do AI tạo ra ở trên để chuẩn bị đánh giá.",
        "missing": "Vui lòng xác nhận đã đọc tuyên bố miễn trừ trách nhiệm trước khi tiếp tục.",
        "rate_help": "Chọn từ 1 (rất kém) đến 5 (xuất sắc). Chọn 3 nếu chưa chắc chắn.",
    }
}

if "language" not in st.session_state:
    st.session_state.language = "English"

# Disclaimer appears before app use, as requested.
st.title("🩺 Medical AI Verification System")
language = st.selectbox("Interface language / Ngôn ngữ giao diện", ["English", "Tiếng Việt"], index=0)
st.session_state.language = language
t = TEXT[language]

st.subheader(t["notice_title"])
st.warning(t["notice"])
ack = st.checkbox(t["ack"], key="disclaimer_ack")
if not ack:
    st.info(t["missing"])
    st.stop()

st.caption(t["subtitle"])
st.divider()

st.header(t["input_title"])
st.caption(t["input_help"])
ai_answer = st.text_area(t["input_label"], height=180, placeholder="Paste the AI-generated health information here...")
claim = st.text_input(t["claim_label"])

st.header(t["source_title"])
st.write(t["source_text"])
search_query = claim.strip() or ai_answer.strip()[:250]
if search_query:
    import urllib.parse
    q = urllib.parse.quote_plus(search_query)
    c1, c2, c3 = st.columns(3)
    c1.link_button("🌐 " + t["who"], "https://www.who.int/search?query=" + q, use_container_width=True)
    c2.link_button("🏛️ " + t["cdc"], "https://search.cdc.gov/search/?query=" + q, use_container_width=True)
    c3.link_button("📚 " + t["nih"], "https://search.nih.gov/search?utf8=%E2%9C%93&affiliate=nih&query=" + q, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    source_name = st.text_input(t["source_name"])
    source_url = st.text_input(t["source_url"])
with col2:
    source_date = st.text_input(t["source_date"], placeholder="e.g., 2025-02-01")
evidence = st.text_area(t["evidence_label"], height=130, help=t["evidence_help"])

st.header(t["assessment_title"])
st.caption(t["assessment_help"])
status_options = [t["supported"], t["contradicted"], t["mixed"], t["insufficient"]]
status = st.radio(t["status"], status_options, index=3, horizontal=False)

st.header(t["review_title"])
st.caption(t["review_help"])
reviewer = st.selectbox(t["reviewer"], t["reviewer_options"])

st.subheader(t["discern_title"])
ratings = []
for i, item in enumerate(t["discern_items"], 1):
    ratings.append(st.slider(f"{i}. {item}", min_value=1, max_value=5, value=3, help=t["rate_help"], key=f"rating_{i}"))
quality_score = sum(ratings)
quality_max = len(ratings) * 5

st.subheader(t["jama_title"])
jama_answers = []
for i, item in enumerate(t["jama_items"], 1):
    jama_answers.append(st.selectbox(item, [t["unknown"], t["yes"], t["no"]], key=f"jama_{i}"))
jama_present = sum(1 for answer in jama_answers if answer == t["yes"])

st.header(t["result_title"])
if not ai_answer.strip() and not claim.strip():
    st.info(t["empty"])
else:
    if status == t["supported"]:
        st.success(t["green"])
        status_color = "GREEN"
    elif status == t["contradicted"]:
        st.error(t["red"])
        status_color = "RED"
    elif status == t["mixed"]:
        st.warning(t["yellow_mixed"])
        status_color = "YELLOW — MIXED"
    else:
        st.warning(t["yellow_insufficient"])
        status_color = "YELLOW — INSUFFICIENT"

    left, right = st.columns(2)
    with left:
        st.metric(t["score"], f"{quality_score} / {quality_max}")
        st.caption(t["score_note"])
    with right:
        st.metric(t["jama_score"], f"{jama_present} / {len(t['jama_items'])}")

    st.markdown(f"**{t['claim']}:**")
    st.write(claim or ai_answer)
    st.markdown(f"**{t['source']}:**")
    st.write(source_name or "Not entered")
    if source_url:
        st.markdown(f"[{source_url}]({source_url})")
    if source_date:
        st.write(f"{t['source_date']}: {source_date}")
    st.markdown(f"**{t['evidence']}:**")
    st.write(evidence or "Not entered")
    st.markdown(f"**{t['status_label']}:** {status_color}")
    st.markdown(f"**{t['reviewer_label']}:** {reviewer}")

    report_lines = [
        t["title"],
        f"Generated: {datetime.now().isoformat(timespec='minutes')}",
        f"{t['claim']}: {claim or ai_answer}",
        f"{t['source']}: {source_name}",
        f"URL: {source_url}",
        f"Source date: {source_date}",
        f"{t['evidence']}: {evidence}",
        f"{t['status_label']}: {status_color}",
        f"{t['reviewer_label']}: {reviewer}",
        f"{t['score']}: {quality_score}/{quality_max}",
        f"{t['jama_score']}: {jama_present}/{len(t['jama_items'])}",
        "",
        t["disclaimer_end"],
    ]
    st.download_button(t["download"], "\n".join(report_lines), file_name="medical_ai_verification_review.txt", mime="text/plain")

st.divider()
st.subheader(t["disclaimer_end_title"])
st.warning(t["disclaimer_end"])

with st.expander("Technical limitations / Giới hạn kỹ thuật"):
    st.write(
        "This prototype opens official-site search pages but does not automatically retrieve, rank, or verify source content. "
        "The reviewer must inspect the source and enter the evidence/status. The DISCERN-inspired questions are adapted and incomplete; "
        "they are not the full validated DISCERN instrument. The JAMA checks are displayed as simple presence/absence checks. "
        "The tool is not clinically validated and must not be used to make diagnosis or treatment decisions."
    )
