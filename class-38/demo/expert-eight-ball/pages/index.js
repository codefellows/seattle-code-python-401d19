import Head from 'next/head';
import { useState } from 'react';
import EightBall from '../components/EightBall';
import Footer from '../components/Footer';
import Header from '../components/Header';
import History from '../components/History';
import QuestionForm from '../components/QuestionForm';
import { replies } from '../data';


export default function Home() {

    const [questions, setQuestions] = useState([]);

    function handleQuestion(question) {
        const randIndex = Math.floor(Math.random() * replies.length);

        const answer = replies[randIndex];

        const questionObj = {
            id: questions.length + 1,
            question: question,
            answer: answer,
        };

        setQuestions([...questions, questionObj]);
    }

    function getAnswer() {
        if (questions.length == 0) {
            return "";
        } else {
            return questions.answer;
        }
    }


    return (
        <>
            <Head>
                <title>Expert Eight Ball</title>
            </Head>
            <div>
                <Header count={questions.length} />
                <QuestionForm onQuestion={handleQuestion} />
                <EightBall answer={getAnswer()} />
                <History questions={questions} />
                <Footer />
            </div>
        </>
    );
}










