import { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import './App.css'

function App() {
  const [request, setRequest] = useState('')
  const [result, setResult] = useState('')
  const [loading, setLoading] = useState(false)
  

  const planTrip = async () => {
    setLoading(true)
    
    const response = await fetch('http://127.0.0.1:8000/plan-trip', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        user_request: request,
      }),
    })

    const data = await response.json()

    setResult(data.trip_plan)
    setLoading(false)
  }

  return (
    <div className="app">
      <h1>AI Travel Planner</h1>

      <p className="subtitle">
        Plan smarter trips with AI agents, live tools, and saved travel history.
      </p>

      <textarea
        placeholder="Plan a 5-day trip to New York"
        value={request}
        onChange={(e) => setRequest(e.target.value)}
      />

      <button onClick={planTrip} disabled={loading}>
      {loading ? 'Planning your trip...' : 'Plan Trip'}
      </button>

      {result && (
        <div className="result-card">
          <h2>Your Trip Plan</h2>
          <ReactMarkdown>{result}</ReactMarkdown>
        </div>
      )}
    </div>
  )
}

export default App