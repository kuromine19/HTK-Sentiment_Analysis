
<div align="center">
  <h1>HTK-Sentiment_Analysis</h1>
</div>
   
<!-- About the Project -->
## :star2: Giới thiệu dự án
- Động lực:

   Số lượng tweet lớn: Twitter là mạng xã hội lớn và phổ biến trên toàn cầu, với hàng triệu
  tweet được đăng tải hàng ngày. Điều này cung cấp một nguồn dữ liệu lớn để xây dựng
  mô hình phân loại nội dung.
  
   Tính đa dạng của nội dung: Trên Twitter, người dùng có thể chia sẻ mọi loại thông tin, từ
  tin tức, giải trí đến ý kiến cá nhân và cảm xúc. Do đó, tweet cung cấp một mẫu đa dạng
  của các loại nội dung phân loại cảm xúc.
  
   Tính ngắn gọn: Tweet có giới hạn ký tự 280, điều này yêu cầu người dùng phải tóm tắt ý
  kiến hoặc cảm xúc của họ trong một khoảng thời gian ngắn. Điều này làm cho tweet rất
  thú vị để phân tích, vì chúng ta cần đánh giá các từ và cụm từ để hiểu ý nghĩa của tweet.
  
   Tính thời sự: Twitter cung cấp một phương tiện để người dùng chia sẻ ý kiến và cảm xúc
  về các sự kiện thời sự đang diễn ra. Điều này cung cấp một cơ hội để xây dựng các mô
  hình phân loại nội dung về các sự kiện thời sự để theo dõi ý kiến của người dùng.

- Mục tiêu: Xây dựng một webapp có tích hợp mô hình dự đoán các cảm xúc được thể hiện trong tweet. 
<!-- TechStack -->
## :space_invader: Các bước thực hiên

<details>
  <summary>Thu thập dữ liệu: Kaggle </summary>
</details>

<details>
  <summary>Xử lý và phân tích dữ liệu: Sử dụng Python để tiền xử lý và tương quan các cột dữ liệu để tìm ra features thích hợp để train mô hình.  </summary>
</details>

<details>
  <summary>Chọn và huấn luyện mô hình: Sử dụng mô hình pre-trained BERT để huấn luyện với dữ liệu thu thập được.</summary>
</details>

<details>
  <summary>Xây dựng webapp để demo chức năng mô hình: Ứng dụng thư viện Streamlit.</summary>
</details>

<!-- Features -->
## :dart: Sản phẩm đầu ra
<p>
     Demo: https://htk-sentimentanalysistweet-3c9bbajdf0w.streamlit.app/
</p>

- Nút “About Group”: Xem thông tin thành viên nhóm.
- Ô nhập dữ liệu: Người dùng nhập câu tweet cần dự đoán.
- Nút “Predict”: Dùng để dự đoán tweet đã nhập.
