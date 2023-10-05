import {BrowserRouter as Router, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import Login from './pages/Login'
import Header from './components/Header'
import LoginPrivateRoute from './utils/LoginPrivateRoute'
import Register from './pages/Register'
import LogoutPrivateRoute from './utils/LogoutPrivateRoute'
import {AuthProvider} from './utils/AuthContext'
import CategoryPage from './pages/Category'

function App() {

  return (
    <>
      <Router>
          <AuthProvider>
              <Header />
              <LoginPrivateRoute component={HomePage} path='/' exact/>
              <LogoutPrivateRoute component={Login} path='/login' exact />
              <LogoutPrivateRoute component={Register} path='/register' exact />
              <Route component={CategoryPage} path='/category/:name' exact/>
          </AuthProvider>
      </Router>
    </>
  )
}

export default App
