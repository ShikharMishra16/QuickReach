import React, { useState } from "react";
import { fetchShortData } from "./callServer";
import Routes from "./routes";
import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";

const ZoomableImage = ({ src, alt }) => {
  return (
    <div className="bg-gray-800/60 rounded-2xl flex flex-col items-center justify-center shadow-xl backdrop-blur-md border border-gray-700 hover:border-indigo-500 transition overflow-hidden p-4">
      <TransformWrapper
        initialScale={1}
        minScale={1}
        maxScale={3}
        wheel={{ step: 0.1 }}
        doubleClick={{ disabled: true }}
        pinch={{ step: 5 }}
      >
        <TransformComponent>
          <img
            src={src}
            alt={alt}
            className="w-full h-auto object-contain rounded-lg cursor-grab"
          />
        </TransformComponent>
      </TransformWrapper>
    </div>
  );
};

const App = () => {
  const [data, setData] = useState(null);
  const [display, setDisplay] = useState(false);

  const onsubmitHandler = async (e) => {
    e.preventDefault();
    const a = e.target.source.value;
    const b = e.target.destination.value;

    try {
      const jsonData = await fetchShortData(a, b);
      setData(jsonData);
      setDisplay(true);
    } catch (error) {
      console.error("Error in submit:", error);
    }

    e.target.reset();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-gray-100 flex flex-col items-center p-8">
      <header className="text-4xl font-extrabold text-indigo-400 mb-10 tracking-wide drop-shadow-lg">
        QuickReach <span className="text-indigo-300">- Shortest Path Finder</span>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8 w-full max-w-6xl mb-12">
        <ZoomableImage src="/satMap.png" alt="Satellite Map" />
        <ZoomableImage src="/outlineMap.png" alt="Output Map" />
      </div>

      <form
        onSubmit={onsubmitHandler}
        className="bg-gray-800/70 shadow-2xl rounded-2xl p-8 w-full max-w-lg space-y-6 border border-gray-700 hover:border-indigo-500 transition"
      >
        <div>
          <label htmlFor="source" className="block text-indigo-300 font-semibold mb-2">
            Source
          </label>
          <input
            id="source"
            name="source"
            type="number"
            min={1}
            max={64}
            placeholder="Enter Source"
            required
            className="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 text-gray-100 placeholder-gray-500 focus:ring-2 focus:ring-indigo-400 focus:outline-none"
          />
        </div>

        <div>
          <label htmlFor="destination" className="block text-indigo-300 font-semibold mb-2">
            Destination
          </label>
          <input
            id="destination"
            name="destination"
            type="number"
            min={1}
            max={64}
            placeholder="Enter Destination"
            required
            className="w-full bg-gray-900 border border-gray-700 rounded-lg px-4 py-3 text-gray-100 placeholder-gray-500 focus:ring-2 focus:ring-indigo-400 focus:outline-none"
          />
        </div>

        <button
          type="submit"
          className="w-full bg-indigo-600 text-white py-3 rounded-lg font-semibold hover:bg-indigo-700 transition duration-300 shadow-lg hover:shadow-indigo-500/40"
        >
          Find Path
        </button>
      </form>

      <div className="w-full max-w-4xl mt-12">
        {display && data && (
          <div className="bg-gray-800/70 rounded-2xl p-6 shadow-xl border border-gray-700">
            <Routes dataPoint={data} />
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
