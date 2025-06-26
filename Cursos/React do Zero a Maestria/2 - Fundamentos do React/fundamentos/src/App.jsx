import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'

// Components
import FirstComponent from './components/FirstComponent.jsx'
import TempleteExpressions from './components/TemplateExpressions.jsx'
import MyComponents from './components/MyComponents.jsx'
import Events from './components/Events.jsx'

// Style (css)
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <h1>Fundamentos React</h1>
     <FirstComponent/>
     <TempleteExpressions/>
     <MyComponents/>
     <Events/>
    </>
  )
}

export default App
