import Head from 'next/head'
import { useState } from 'react'

export default function Home() {

    const [question, setQuestion] = useState("Ask me anything...");
    const [reply, setReply] = useState("Thinking...")

    function questionAskedHandler(event) {
        event.preventDefault();
        let randomReply = Math.random() > .5 ? "Yes" : "No";
        setQuestion(event.target.question.value);
        setReply(randomReply)
        event.target.reset()
    }
    return (
        <div>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <Header />
            <main className="flex flex-col items-center py-4 space-y-8">
                <QuestionForm onSubmit={questionAskedHandler} />
                <EightBall question={question} />
                <Response reply={reply} />
            </main>
            <Footer copyright="2022" />
        </div>
    )
}

function EightBall({ question }) {
    return <div className="bg-gray-900 rounded-full w-96 h-96">
        <div className="relative flex items-center justify-center w-56 h-56 rounded-full bg-gray-50 left-12 top-12">
            <p>{question}</p>
        </div>
    </div>
}

function Header() {
    return <header className="px-8 py-6 text-4xl bg-gray-500 text-gray-50">
        <h1>Expert 8 Ball</h1>
    </header>
}

function QuestionForm(props) {
    return (
        <form onSubmit={props.onSubmit} className="flex w-1/2 p-2 bg-gray-200">
            <input name="question" className="flex-auto pl-2" placeholder='Ask me anything...' required />
            <button className="px-4 py-2 bg-gray-400 text-gray-50">Ask</button>
        </form>
    )
}

function Response({ reply }) {
    return <p className="">{reply}</p>
}

function Footer({ copyright }) {
    return (
        <footer className="px-8 py-6 bg-gray-500 text-gray-50">
            <p>&copy;{copyright}</p>
        </footer>
    )
}

