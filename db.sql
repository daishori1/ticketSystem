CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE staff (
    id_staff SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    team VARCHAR(50) NOT NULL,
    rol VARCHAR(50) NOT NULL
);

CREATE TABLE tikets (
    tiket_id SERIAL PRIMARY KEY,
    user_request INT,
    status VARCHAR(30) DEFAULT 'open',
    tiket_content TEXT,
    due_date DATE,
    assigned_to INT,
    team VARCHAR(30),
    affected VARCHAR(30),
    tiket_creation_date DATE DEFAULT CURRENT_DATE,
    tiket_close_date DATE,
    FOREIGN KEY (user_request) REFERENCES users(user_id),
    FOREIGN KEY (assigned_to) REFERENCES staff(id_staff)
);




-- Users
INSERT INTO users  VALUES
(default,'Mayeli jasso', 'mayeli33salccedo@gamil.com'),
(default,'Juan Perez', 'juan@email.com'),
(default,'Maria Garcia', 'maria@email.com');

-- Staff
INSERT INTO staff  VALUES
(default ,'Carlos Mendez', 'carlos@empresa.com', 'IT', 'SysAdmin'),
(default ,'Ana Torres', 'ana@empresa.com', 'developers', 'Backend Dev'),
(default ,'Luis Ramos', 'luis@empresa.com', 'IT', 'On Site Technician');

-- Tikets
INSERT INTO tikets (user_request, status, tiket_content, due_date, assigned_to, team, affected) VALUES
(default, 'open', 'VPN caida, usuario no puede conectarse remotamente', '2026-06-20', 1, 'IT', 'Mayeli jasso '),
(default, 'open', 'Pantalla azul en equipo de trabajo', '2026-06-18', 3, 'IT', 'Juan Perez'),
(default, 'closed', 'Impresora offline en piso 2', '2026-06-15', 1, 'IT', 'Maria Garcia');