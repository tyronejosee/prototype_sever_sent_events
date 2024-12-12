import { useEffect, useState } from "react";

const EventStream = () => {
  const [events, setEvents] = useState<string[]>([]);

  useEffect(() => {
    const eventSource = new EventSource("http://localhost:8000/sse/");

    eventSource.onmessage = (event) => {
      setEvents((prevEvents) => [...prevEvents, event.data]);
    };

    eventSource.onerror = (err) => {
      console.error("Stream Error:", err);
      eventSource.close(); // Closes the connection if an error occurs
    };

    return () => {
      eventSource.close(); // Cleans up the connection when the component unmounts
    };
  }, []);

  return (
    <section>
      <ul>
        {events.map((event, index) => (
          <li key={index}>{event}</li>
        ))}
      </ul>
    </section>
  );
};

export default EventStream;
