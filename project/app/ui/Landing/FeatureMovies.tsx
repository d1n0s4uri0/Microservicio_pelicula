import { Movie } from "../../types/movie.js";

export default function FeatureMovies({ movies }: { movies: Movie[] }) {
  return (
    <section>
      <h3>Fetarure Movies</h3>

      <div className="flex  gap-4">
        {movies.map((movie, index) => (
          <div
            key={movie.id}
            className="h-[400] w-[350px] relative overflow-hidden rounded-xl shadow-xl"
          >
            <img
              className="w-10/12 mx-auto h-full object-cover hover:scale-105 transition-transform duration-500"
              src={movie.posterUrl}
              alt={movie.title}
            />
            <p className="font-bold text-8xl absolute bottom-5">{index + 1}</p>
          </div>
        ))}
      </div>
    </section>
  );
}
