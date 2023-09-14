import { useState } from "react";

function App() {
  const [response, setResponse] = useState("");

  const getPrompt = () => {
    return (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      const recipient = (e.target as HTMLFormElement).recipient.value;
      const topic = (e.target as HTMLFormElement).topic.value;

      // ENTER YOUR URL HERE
      const url = new URL("http://localhost:8000/get-email/");

      url.searchParams.append("name", recipient);
      url.searchParams.append("theme", topic);

      fetch(url.toString())
        .then((res) => res.json())
        .then((data) => {
          setResponse((data.email_text as string).trimStart());
        });
    };
  };

  return (
    <div className="p-4 flex flex-col gap-6 max-w-3xl">
      <form className="flex flex-col gap-4 max-w-xs" onSubmit={getPrompt()}>
        <div className="flex flex-col">
          <label htmlFor="" className="font-semibold">
            Email Recipient
          </label>
          <input
            type="text"
            name="recipient"
            id="recipient"
            placeholder="Enter the recipient's name"
            className="border border-gray-300 rounded-md px-4 py-2 mt-2 "
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="emailTopic" className="font-semibold">
            Email Topic
          </label>
          <input
            type="text"
            name="topic"
            id="emailTopic"
            placeholder="Enter the email topic"
            className="border border-gray-300 rounded-md px-4 py-2 mt-2 "
          />
        </div>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-md"
          type="submit"
        >
          Get Email
        </button>
      </form>
      {response && (
        <div className="flex flex-col gap-4">
          <label htmlFor="" className="font-semibold">
            Email
          </label>
          <p className="border-gray-200 border-2 rounded-md p-4">
            {response.split("\n").map((line, i) => (
              <span key={i}>
                {line}
                <br />
              </span>
            ))}
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
