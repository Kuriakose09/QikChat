import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>QuickChat</h1>
      </header>
      <div className="chat-container">
        <div className="sidebar">
          <h3>Online Users</h3>
          {/* User list will go here */}
        </div>
      </div>
      <div className="chat-area">
        <div className="messages">
          {/* Messages will appear here */}
        </div>
        <div className="message-input">
          <input type="text" placeholder="Type a message..." />
          <button>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
