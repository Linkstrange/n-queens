-- Table: public.solutions

-- DROP TABLE public.solutions;

CREATE TABLE public.solutions
(
  solution_id bigserial, -- A unique id for this solution
  board_size smallint, -- Size of the board this solution applies to
  solution_ordinal integer, -- Order in wich this solution was stored
  board_hash bigint, -- Hash for the board that has this solution to avoid duplicates
  CONSTRAINT pk_solutions PRIMARY KEY (solution_id),
  CONSTRAINT unique_board_hash UNIQUE (board_hash)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.solutions
  OWNER TO postgres;
COMMENT ON TABLE public.solutions
  IS 'Table used to store solutions for the n queens problem';
COMMENT ON COLUMN public.solutions.solution_id IS 'A unique id for this solution';
COMMENT ON COLUMN public.solutions.board_size IS 'Size of the board this solution applies to';
COMMENT ON COLUMN public.solutions.solution_ordinal IS 'Order in wich this solution was stored';
COMMENT ON COLUMN public.solutions.board_hash IS 'Hash for the board that has this solution to avoid duplicates';

-- Table: public.placements

-- DROP TABLE public.placements;

CREATE TABLE public.placements
(
  placement_id bigserial, -- Id for this placement
  solution_id bigint, -- Id of the solution this placement belongs to
  "row" smallint,
  "column" smallint,
  CONSTRAINT pk_placement PRIMARY KEY (placement_id),
  CONSTRAINT fk_solution_id FOREIGN KEY (solution_id)
      REFERENCES public.solutions (solution_id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE CASCADE
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.placements
  OWNER TO postgres;
COMMENT ON COLUMN public.placements.placement_id IS 'Id for this placement';
COMMENT ON COLUMN public.placements.solution_id IS 'Id of the solution this placement belongs to';


