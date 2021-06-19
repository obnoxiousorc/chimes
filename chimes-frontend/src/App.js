import { Container } from '@material-ui/core';
import './App.css';
import SongList from './SongList';

function App() {
	return (
		<div className="App">
			<Container>
				<SongList />
			</Container>
		</div>
	);
}

export default App;
