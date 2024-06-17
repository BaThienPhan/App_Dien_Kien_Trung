import streamlit as st
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
import altair as alt

# Cài đặt trang
st.set_page_config(page_title="Di tích Điện Kiến Trung Huế", page_icon=":classical_building:", layout="wide")

# CSS tùy chỉnh
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-size: 3em;
        margin-bottom: 20px;
    }
    .header {
        color: #2c3e50;
        font-size: 2em;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .text {
        color: #555555;
        font-size: 1.2em;
        line-height: 1.6;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888888;
    }
    .image-caption {
        text-align: center;
        font-style: italic;
        color: #888888;
        font-size: 0.9em;
        margin-top: -10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("ĐIỆN KIẾN TRUNG")
page = st.sidebar.selectbox("Chọn trang", ["Vị trí địa lí", "Lịch sử", "Kiến trúc", "Du lịch", "Liên hệ"])

# Hàm tải ảnh từ URL
def load_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

# Hiển thị ảnh sử dụng Streamlit
st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/Dienkientrung1.jpg"), caption="Hình ảnh 1", use_column_width=True)
st.markdown("<div class='image-caption'>Điện Kiến Trung sau 4 năm trùng tu. Ảnh: VnExpress</div>", unsafe_allow_html=True)

# Nội dung chính
if page == "Vị trí địa lí":
    st.markdown("<div class='title'>Di tích Điện Kiến Trung Huế</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header'>Giới thiệu</div>
    <div class='text'>
    Điện Kiến Trung là một trong những di tích lịch sử nổi tiếng tại Huế, Việt Nam. Điện Kiến trung nằm trong khôn viên Hoàng Thành Huế. 
    Nằm ở điểm cực bắc của trục thần đạo xuyên qua trung tâm Tử Cấm thành. 
    </div>
    """, unsafe_allow_html=True)
elif page == "Lịch sử":
    st.markdown("<div class='title'>Lịch sử Điện Kiến Trung</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header'>Lịch sử</div>
    <div class='text'>
    Điện Kiến Trung nằm trên mảnh đất sau cuối của Tử Cấm thành, ngay phía sau cung Khôn Thái. Dưới thời vua Minh Mạng, nơi đây có một công trình mang tên là lầu Minh Viễn (chữ Hán: 明遠樓; tồn tại từ 1827-1876).
    Đến thời vua Duy Tân, công trình được kiến tạo và mang tên lầu Du Cửu (1913-1916). Kiến Trung là tên được vua Khải Định đặt từ năm 1916.
    Năm 1921, Điện Kiến Trung được vua Khải Định xây lại mới. Đây cũng là nơi vua Khải Định băng hà vào ngày 6 tháng 11, 1925.
    Sang triều vua kế vị là Bảo Đại thì triều đình cho tu sửa lại tòa điện, tân trang các tiện nghi theo thể cách Tây phương, trong đó có xây buồng tắm.
    Vua và hoàng hậu Nam Phương sau đó dọn về sống trong điện Kiến Trung. Tại điện này, Hoàng hậu Nam Phương hạ sanh Thái tử Bảo Long (4-1-1936).
    Ba người con sau thì sanh ở Đà Lạt (Công chúa Phương Mai 1-8-1937; Công chúa Phương Liên 3-11-1938 và Hoàng tử Bảo Thắng 9-12-1943). Riêng Công chúa Phương Dung sanh ở Cung An Định (5-2-1942).
    Ngày 9 tháng 3, Quân đội Đế quốc Nhật Bản đảo chính chính quyền thuộc địa Đông Pháp và thỏa thuận trao trả độc lập cho Việt Nam.
    Hai ngày sau, 11 Tháng Ba vua Bảo Đại triệu cố vấn tối cao của Nhật là đại sứ Yokoyama Masayuki vào điện Kiến Trung để tuyên bố nước Việt Nam độc lập, khai sinh Đế quốc Việt Nam.
    Cùng đi với Yokoyama là tổng lãnh sự Konagaya Akira và lãnh sự Watanabe Taizo.
    Sang Tháng Tám năm 1945 khi Việt Minh đoạt chính quyền ở Hà Nội thì lực lượng Quân đội Đế quốc Nhật Bản đề nghị phòng thủ điện Kiến Trung chống lại Việt Minh nhưng vua Bảo Đại bác đi vì không muốn đổ máu.
    Điện Kiến Trung sau đó đã bị phá huỷ Tháng Chạp năm 1946 bởi Việt Minh trong chiến lược tiêu thổ kháng chiến, chỉ còn nền điện và hàng lan can trong khu vực Tử Cấm Thành.
    </div>
    """, unsafe_allow_html=True)
elif page == "Kiến trúc":
    st.markdown("<div class='title'>Kiến trúc Điện Kiến Trung</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header'>Kiến trúc</div>
    <div class='text'>
    Từ năm 2013, Trung tâm Bảo tồn di tích cố đô Huế đã khởi động dự án phục hồi điện Kiến Trung, với sự hợp tác của nhiều nhà nghiên cứu về lịch sử, văn hóa và mỹ thuật Huế và sự tham gia của Phân viện khoa học công nghệ xây dựng Miền Trung.
    Dự án phục dựng Điện Kiến Trung dự kiến bắt đầu năm 2018 và hoàn thành vào năm 2020 tuy nhiên đã có một số phản biện về việc phục dựng sai lệch với bản gốc. 
    Cuối cùng dự án này đã được khởi công vào ngày 16 tháng 2 năm 2019 với tổng kinh phí hơn 123 tỉ đồng dự kiến hoàn tất vào tháng 8 năm 2023.
    Điện Kiến Trung nổi bật với kiến trúc độc đáo, kết hợp giữa phong cách truyền thống Việt Nam và ảnh hưởng của kiến trúc phương Tây.
    Kiểu thức điện là hợp thể phong cách Âu châu gồm kiến trúc Pháp, kiến trúc Phục hưng của Ý cùng pha thêm kiến trúc cổ truyền Việt Nam. 
    Mặt tiền điện có trang trí những mảnh gốm sứ nhiều màu. Trước điện là vườn cảnh, có ba cầu thang đắp rồng dẫn lên thềm điện. 
    Tầng chính trổ 13 cửa hiên: gian giữa 5 cửa, hai gian bên mỗi gian 3 cửa, hai góc điện mỗi bên hai cửa nữa làm nhô ra hẳn.
    Tầng trên là gác, làm cùng một thể thức như tầng chính. Trên cùng là mái ngói có hàng lan can trang trí theo phong cách Việt Nam.
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/AnhKhai2.jpg"), caption="Hình ảnh 1", use_column_width=True)
    with col2:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/Dienkientrung2.jpg"), caption="Hình ảnh 2", use_column_width=True)
    with col3:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/Dienkientrung3.jpg"), caption="Hình ảnh 3", use_column_width=True)
elif page == "Du lịch":
    st.markdown("<div class='title'>Thống kê về Điện Kiến Trung</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header'>Thống kê</div>
    <div class='text'>
    Dưới đây là một số hình ảnh du khách và các sự kiện diễn ra tại Điện Kiến Trung.
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/AnhKhai2.jpg"), caption="Hình ảnh 1", use_column_width=True)
    with col2:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/Dienkientrung2.jpg"), caption="Hình ảnh 2", use_column_width=True)
    with col3:
        st.image(load_image("https://github.com/BaThienPhan/DienKienTrung/raw/main/Dienkientrung3.jpg"), caption="Hình ảnh 3", use_column_width=True)
elif page == "Liên hệ":
    st.markdown("<div class='title'>Liên hệ</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='header'>Liên hệ</div>
    <div class='text'>
    Nếu bạn có bất kỳ câu hỏi nào hoặc muốn biết thêm thông tin, vui lòng liên hệ với chúng tôi qua email: example@example.com
    </div>
    """, unsafe_allow_html=True)
    # Form liên hệ
    with st.form(key='contact_form'):
        name = st.text_input("Tên của bạn")
        email = st.text_input("Email của bạn")
        message = st.text_area("Tin nhắn")
        submit_button = st.form_submit_button(label='Gửi')

        if submit_button:
            st.success("Cảm ơn bạn đã liên hệ với chúng tôi!")

# Footer
st.markdown("""
<div class='footer'>
© 2024 Di tích Điện Kiến Trung Huế. All rights reserved.
</div>
""", unsafe_allow_html=True)