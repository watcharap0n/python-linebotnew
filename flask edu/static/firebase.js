var firebaseConfig = {
apiKey: "AIzaSyBlJADiWxXWv6UQMl-bVbsI4fIcpYw8flg",
authDomain: "chatbot-return.firebaseapp.com",
databaseURL: "https://chatbot-return.firebaseio.com",
projectId: "chatbot-return",
storageBucket: "chatbot-return.appspot.com",
messagingSenderId: "102505580300",
appId: "1:102505580300:web:c89f95d84dd17700e1eb29",
measurementId: "G-GQ1BFCVTZN"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.database();
const auth = firebase.auth();
