### CREATE KAFKA CLUSTER
---
![Nodes](./images/Screenshot%20from%202023-04-20%2010-04-00.png)
![Topics](./images/Screenshot%20from%202023-04-20%2010-04-30.png)
- Create topic with option
```
kafka-topics --create --zookeeper zookeeper:2181 --topic <topic_name> --partitions 6 --replication-factor 2
```
![create topic with its options](./images/Screenshot%20from%202023-04-20%2009-31-18.png)
- Test replicate partition of topics
```
kafka-topics --describe --topic <topic-name> --bootstrap-server kafka1:19091
```
![Topic Information](./images/Screenshot%20from%202023-04-20%2009-31-32.png)

- "test" là tên của topic.
- "Partition: 0" cho biết rằng đây là phân vùng số 0 của topic
- "Leader: 3" cho biết rằng broker số 3 là người đứng đầu (leader) cho phân vùng này, có nghĩa là nó chịu trách nhiệm xử lý tất cả các yêu cầu đọc và ghi dữ liệu cho phân vùng này.
- "Replicas: 3,2" cho biết rằng phân vùng này có hai bản sao: một trên broker số 3 và một trên broker số 2. Việc sao chép đảm bảo rằng nếu một broker bị lỗi, sẽ có những broker khác có thể tiếp tục phục vụ yêu cầu cho phân vùng này.
- "Isr: 3,2" cho biết rằng cả hai bản sao số 3 và số 2 đều là các bản sao được đồng bộ hóa (in-sync replica - ISR) với leader. Điều này có nghĩa là chúng đã hoàn toàn đồng bộ với leader và sẵn sàng tiếp quản vai trò leader nếu leader hiện tại gặp sự cố.
---
### Clean Policy
- Clean policy trong Kafka là một cấu hình để quy định cách Kafka sẽ giải quyết các message đã bị xóa hoặc expire. Có hai loại clean policy:

    - Delete: khi một message đã bị xóa hoặc expire, Kafka sẽ xoá nó khỏi partition.

    - Compact: khi một message đã bị xóa hoặc expire, Kafka sẽ giữ lại key của message và xoá toàn bộ các value có cùng key trong partition trước đó, nhằm giảm dung lượng lưu trữ.

- Việc sử dụng clean policy phụ thuộc vào ứng dụng của bạn và yêu cầu kinh tế về bộ nhớ và lưu trữ. Nếu ứng dụng của bạn không cần giữ lại message đã bị xoá hoặc expire, bạn có thể chọn Delete. Tuy nhiên, nếu ứng dụng của bạn cần giữ lại các thông tin thay đổi (ví dụ: theo dõi trạng thái của một entity), bạn có thể chọn Compact.