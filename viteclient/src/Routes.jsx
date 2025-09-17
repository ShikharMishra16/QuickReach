import React from "react";

const Routes = ({ dataPoint }) => {
  return (
    <div className="w-full bg-gray-800/70 border border-gray-700 rounded-2xl shadow-xl p-8 space-y-6 hover:border-indigo-500 transition">
      
      {/* Source */}
      <div className="flex items-center gap-3">
        <span className="font-semibold text-indigo-300">Source:</span>
        <span className="text-gray-100 font-medium">{dataPoint.from}</span>
      </div>

      {/* Destination */}
      <div className="flex items-center gap-3">
        <span className="font-semibold text-indigo-300">Destination:</span>
        <span className="text-gray-100 font-medium">{dataPoint.to}</span>
      </div>

      {/* Path */}
      <div>
        <span className="font-semibold text-indigo-300 block mb-3">Path:</span>
        <div className="flex flex-wrap gap-3">
          {dataPoint.path.map((node, index) => (
            <div
              key={index}
              className="px-4 py-1.5 bg-indigo-600/20 border border-indigo-400/40 text-indigo-200 rounded-full text-sm font-semibold shadow-md hover:bg-indigo-500/30 hover:text-white transition"
            >
              {node}
            </div>
          ))}
        </div>
      </div>

      {/* Distance */}
      <div className="flex items-center gap-3">
        <span className="font-semibold text-indigo-300">Distance:</span>
        <span className="text-gray-100 font-medium">{dataPoint.totalDis} m</span>
      </div>
    </div>
  );
};

export default Routes;
