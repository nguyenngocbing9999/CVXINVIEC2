import streamlit as st
from pathlib import Path

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="CV - Nguyễn Ngọc Bình",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
PHOTO = BASE / "profile.jpg"

# =========================
# CSS - GIAO DIỆN GIỐNG CV
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap');

:root{
    --navy:#243b78;
    --cyan:#39c7e8;
    --text:#253a78;
    --light:#f7f8fb;
}

html, body, [class*="css"] {
    font-family: 'Montserrat', Arial, sans-serif;
}

.stApp {
    background: #ffffff;
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}

/* Navigation */
.nav-wrap {
    display:flex;
    justify-content:center;
    gap:10px;
    margin: 0 0 18px 0;
}
.nav-title {
    text-align:center;
    font-weight:800;
    font-size:28px;
    color:var(--navy);
    margin-bottom:4px;
}
.nav-sub {
    text-align:center;
    color:#666;
    margin-bottom:16px;
}

/* CV */
.cv {
    display:grid;
    grid-template-columns: 36% 64%;
    min-height: 1200px;
    box-shadow: 0 4px 25px rgba(0,0,0,.10);
    border-radius: 4px;
    overflow:hidden;
}

.left {
    background:var(--navy);
    color:white;
    padding:30px 26px 36px 26px;
}

.right {
    background:white;
    color:var(--text);
    padding:34px 38px;
}

.profile {
    width:270px;
    height:270px;
    object-fit:cover;
    border-radius:50%;
    display:block;
    margin:0 auto 24px auto;
    border:4px solid white;
}

.name {
    color:var(--cyan);
    font-size:29px;
    font-weight:800;
    text-align:center;
    letter-spacing:.4px;
    margin:8px 0 8px;
}
.role {
    color:white;
    text-align:center;
    font-size:17px;
    letter-spacing:2px;
    margin-bottom:38px;
}

.left-heading {
    color:var(--cyan);
    text-align:center;
    font-weight:800;
    font-size:21px;
    letter-spacing:1.2px;
    margin:27px 0 12px;
}
.left ul {
    margin-top:0;
    padding-left:22px;
}
.left li {
    margin-bottom:7px;
    line-height:1.38;
    font-size:15px;
}

.section-title {
    background:var(--navy);
    color:var(--cyan);
    text-align:center;
    font-size:21px;
    font-weight:800;
    letter-spacing:1px;
    padding:9px 12px;
    margin:0 0 24px 0;
}
.edu-title {
    color:var(--cyan);
    font-size:21px;
    margin-bottom:10px;
}
.right p, .right li {
    font-size:16px;
    line-height:1.48;
}
.right ul {
    padding-left:22px;
}
.job-title {
    color:var(--cyan);
    font-size:20px;
    margin-bottom:5px;
}
.job-meta {
    display:flex;
    justify-content:space-between;
    color:var(--cyan);
    font-size:16px;
    margin-bottom:12px;
}
.divider {
    height:1px;
    background:#e8e8e8;
    margin:24px 0;
}

/* Letter */
.letter {
    box-shadow: 0 4px 25px rgba(0,0,0,.10);
    background:white;
    overflow:hidden;
}
.letter-header {
    background:var(--navy);
    color:white;
    padding:24px 48px 22px 48px;
    position:relative;
    min-height:150px;
}
.letter-photo {
    width:170px;
    height:170px;
    object-fit:cover;
    border-radius:50%;
    position:absolute;
    left:35px;
    top:15px;
    border:4px solid white;
}
.letter-head-text {
    margin-left:230px;
}
.letter-name {
    font-size:29px;
    font-weight:800;
    margin-bottom:7px;
}
.letter-role {
    font-size:18px;
    letter-spacing:1.5px;
    margin-bottom:18px;
}
.contact {
    font-size:14px;
    line-height:1.7;
}
.letter-body {
    padding:28px 48px 45px 48px;
    color:#111;
}
.date {
    text-align:center;
    font-size:17px;
    font-weight:600;
    margin-bottom:15px;
}
.letter-title {
    text-align:center;
    font-size:21px;
    font-weight:800;
    margin-bottom:36px;
}
.letter-body p {
    font-size:16px;
    line-height:1.65;
    margin-bottom:22px;
    text-align:justify;
}
.signature {
    text-align:right;
    margin-top:22px;
    font-size:16px;
    line-height:1.7;
}

@media (max-width: 850px) {
    .cv { grid-template-columns:1fr; }
    .left { padding:25px 22px; }
    .right { padding:25px 22px; }
    .letter-head-text { margin-left:0; margin-top:185px; }
    .letter-photo { position:relative; left:auto; top:auto; display:block; margin:0 auto 20px; }
    .letter-header { text-align:center; }
    .job-meta { display:block; }
}
</style>
""", unsafe_allow_html=True)

# =========================
# TIÊU ĐỀ
# =========================
st.markdown('<div class="nav-title">NGUYỄN NGỌC BÌNH</div>', unsafe_allow_html=True)
st.markdown('<div class="nav-sub">HỒ SƠ ỨNG TUYỂN – CHUYÊN VIÊN TÍN DỤNG CÁ NHÂN</div>', unsafe_allow_html=True)

tab_cv, tab_letter = st.tabs(["📄 CV", "✉️ THƯ ỨNG TUYỂN"])

# =========================
# TAB 1 - CV
# =========================
with tab_cv:
    st.markdown('<div class="cv">', unsafe_allow_html=True)

    # Cột trái
    st.markdown('<div class="left">', unsafe_allow_html=True)

    if PHOTO.exists():
        st.image(str(PHOTO), width=270)

    st.markdown('<div class="name">NGUYỄN NGỌC BÌNH</div>', unsafe_allow_html=True)
    st.markdown('<div class="role">CHUYÊN VIÊN TÍN DỤNG CÁ NHÂN</div>', unsafe_allow_html=True)

    st.markdown('<div class="left-heading">THÔNG TIN CÁ NHÂN</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
      <li>Điện thoại: 0972628063</li>
      <li>Email: nguyengocbing9999@gmail.com</li>
      <li>Địa chỉ: 213, Tổ 6, Phú Thịnh, Xã Phú Riềng, Tỉnh Đồng Nai.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="left-heading">SỞ THÍCH</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
      <li>Thích đọc sách, chơi thể thao</li>
      <li>Tình nguyện viên, hoạt động cộng đồng</li>
      <li>Thích trải nghiệm và học hỏi</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="left-heading">KỸ NĂNG LÀM VIỆC</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
      <li>Tư vấn &amp; Giao tiếp</li>
      <li>Bán hàng &amp; Chăm sóc Khách hàng</li>
      <li>Kiến thức Tài chính</li>
      <li>Kỹ năng tổ chức, làm việc nhóm</li>
      <li>Quản lý thời gian</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="left-heading">CHỨNG CHỈ</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul>
      <li>Bằng Tiếng Anh nội bộ</li>
      <li>Chứng chỉ Tin học văn phòng</li>
      <li>Chứng chỉ soạn thảo văn bản</li>
      <li>Chứng chỉ Kỹ năng giao tiếp</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Cột phải
    st.markdown('<div class="right">', unsafe_allow_html=True)

    st.markdown('<div class="section-title">MỤC TIÊU CÔNG VIỆC</div>', unsafe_allow_html=True)
    st.markdown("""
    <p>
    Mong muốn trở thành một Chuyên viên Tín dụng chủ chốt tại Quý Ngân hàng.
    Trong 1-2 năm đầu, tôi sẽ tập trung vào việc thực hiện thành thạo quy trình
    nghiệp vụ, xây dựng danh mục khách hàng chất lượng cao, và đạt/vượt các KPI kinh doanh.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">HỌC VẤN</div>', unsafe_allow_html=True)
    st.markdown('<div class="edu-title">Đại học Nguyễn Tất Thành</div>', unsafe_allow_html=True)
    st.markdown("""
    <p style="margin-bottom:8px;">
      Cử nhân Tài chính - Kế toán<br>
      Tháng 9/2023 - 12/2026
    </p>
    <ul>
      <li>Cử nhân: Tài chính - Kế toán</li>
      <li>GPA: 3,00</li>
      <li>Chuyên ngành Tài chính Ngân hàng</li>
      <li>Thời gian: 3/2023 - 12/2026 (dự kiến tốt nghiệp)</li>
      <li>Kiến tập thực tế: Đã tham gia chương trình Kiến tập tại Ngân hàng TMCP VietBank.</li>
      <li>Nghiên cứu Chuyên ngành: Chủ động thực hiện nhiều bài nghiên cứu chuyên sâu, tiểu luận về các vấn đề trong ngành ngân hàng và tài chính.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">KINH NGHIỆM LÀM VIỆC</div>', unsafe_allow_html=True)
    st.markdown('<div class="job-title">Kỹ thuật viên/Dịch vụ khách hàng</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="job-meta">
      <span>SPA Vật lí trị liệu MH</span>
      <span>9/2023 - 10/2024</span>
    </div>
    <ul>
      <li>Giao tiếp trực tiếp và xây dựng lòng tin với khách hàng để tư vấn các gói dịch vụ.</li>
      <li>Thực hiện bán chéo (cross-selling) các sản phẩm bổ sung và duy trì quan hệ khách hàng để tăng doanh số.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">NGOẠI NGỮ</div>', unsafe_allow_html=True)
    st.markdown('<p>Tiếng Anh giao tiếp cơ bản</p>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# =========================
# TAB 2 - THƯ ỨNG TUYỂN
# =========================
with tab_letter:
    st.markdown('<div class="letter">', unsafe_allow_html=True)
    st.markdown('<div class="letter-header">', unsafe_allow_html=True)

    if PHOTO.exists():
        st.image(str(PHOTO), width=170)

    st.markdown("""
    <div class="letter-head-text">
      <div class="letter-name">NGUYỄN NGỌC BÌNH</div>
      <div class="letter-role">CHUYÊN VIÊN TÍN DỤNG CÁ NHÂN</div>
      <div class="contact">
        ☎ &nbsp;0972628063<br>
        ✉ &nbsp;nguyengocbing9999@gmail.com<br>
        ⌖ &nbsp;213, Tổ 6, Phú Thịnh, Xã Phú Riềng, Tỉnh Đồng Nai.
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="letter-body">', unsafe_allow_html=True)

    st.markdown('<div class="date">Ngày 4 tháng 12 năm 2025</div>', unsafe_allow_html=True)
    st.markdown('<div class="letter-title">Thư ứng tuyển vị trí Chuyên viên Tín dụng Cá nhân</div>', unsafe_allow_html=True)

    st.markdown("""
    <p>
    Kính gửi chị Nguyễn Thị A - Trưởng phòng Hành chính Nhân sự của Ngân hàng TMCP Việt Nam
    Thịnh Vượng VPBank Trụ sở TP.HCM Việt Nam.
    </p>

    <p>
    Tôi là Nguyễn Ngọc Bình, sinh viên mới tốt nghiệp ngành Tài chính Ngân hàng tại Trường đại học
    Nguyễn Tất Thành TP.HCM.<br>
    Thông qua website CareerViet, tôi được biết Quý Ngân hàng đang có nhu cầu ứng tuyển nhân sự
    cho vị trí Chuyên viên Tín dụng Cá nhân, tôi nhận thấy đây là công việc hoàn toàn phù hợp với định
    hướng phát triển nghề nghiệp của tôi trong lĩnh vực tư vấn bán hàng. Với kiến thức nền tảng vững
    chắc và niềm đam mê đặc biệt đối với chuyên ngành Tài chính, tôi rất mong muốn được ứng tuyển
    vào vị trí này tại VPBank - một trong những ngân hàng bán lẻ hàng đầu Việt Nam.
    </p>

    <p>
    Tôi đặc biệt ấn tượng với VPBank bởi tầm nhìn chiến lược và sự năng động, tiên phong trong việc
    cung cấp các giải pháp tài chính cá nhân hiện đại và linh hoạt.<br>
    Vị trí Chuyên viên Tín dụng Cá nhân không chỉ là cơ hội để tôi áp dụng kiến thức phân tích tài chính
    và quản trị rủi ro đã được đào tạo chuyên sâu tại Trường Đại học mà còn là môi trường lý tưởng để
    tôi phát triển kỹ năng tư vấn, thuyết phục và đạt chỉ tiêu kinh doanh đồng thời đóng góp trực tiếp vào
    sự phát triển của Ngân hàng.
    </p>

    <p>
    Trong suốt quá trình học tập, tôi đã tích lũy được kiến thức chuyên sâu về Phân tích Tài chính,
    Quản trị rủi ro Tín dụng và Nghiệp vụ Ngân hàng bán lẻ.<br>
    Tôi đã hoàn thành xuất sắc môn học Đánh giá Tín dụng và Quản trị rủi ro Tài chính, nắm vững quy
    trình thẩm định hồ sơ, đánh giá khả năng trả nợ của khách hàng cá nhân.<br>
    Bên cạnh đó tôi là người cẩn thận, cầu tiến và có tinh thần trách nhiệm cao. Tôi cam kết học hỏi
    nhanh chóng, áp dụng kiến thức đã có và đóng góp vào mục tiêu kinh doanh của quý Ngân hàng.
    </p>

    <p>
    Tôi rất mong có cơ hội được trình bày chi tiết hơn về tiềm năng và sự phù hợp của tôi đối với vị trí
    Chuyên viên Tín dụng Cá nhân trong một buổi phỏng vấn trực tiếp.<br>
    Xin chân thành cảm ơn Quý Ngân hàng đã dành thời gian xem xét hồ sơ của tôi.
    </p>

    <div class="signature">
      Trân trọng<br>
      <strong>Nguyễn Ngọc Bình</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<div style="text-align:center;color:#888;font-size:12px;margin-top:18px;">
CV được chuyển đổi thành ứng dụng Streamlit từ nội dung tài liệu được cung cấp.
</div>
""", unsafe_allow_html=True)
