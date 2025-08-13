import React, { useState} from 'react';
import './BookComponent.css';

const BookComponent = ({ pages }) => {
    const [currentPage, setCurrentPage] = useState(0);
    const [isFlipping, setIsFlipping] = useState(false);

    const nextPage = () => {
        if (currentPage < pages.length -1 && !isFlipping) {
            setIsFlipping(true);
            setTimeout(() => {
                setCurrentPage(currentPage + 1);
                setIsFlipping(false);
            }, 500);
        }
    };

    const previousPage = () => {
        if (currentPage > 0 && !isFlipping) {
            setIsFlipping(true);
            setTimeout(() => {
                setCurrentPage(currentPage - 1);
                setIsFlipping(false);
            }, 500);
        }
    };

    return (
        <div className='book-container'>
            <div className={`book ${isFlipping ? 'flipping': ''}`}>
                <div className="page current-page">
                    <div className="page-content">
                        <h2 className="chapter-title">Capítulo {currentPage +1}</h2>
                        {pages[currentPage]}
                    </div>
                </div>
                <div className="book-spine"></div>
            </div>

            <div className="book-controls">
                <button
                onClick={previousPage}
                disabled={currentPage === 0 || isFlipping}
                className="book-btn"
                >
                    ← Anterior
                </button>
                <span className="page-number">
                    Página {currentPage +1} de {pages.length}
                </span>
                <button
                onClick={nextPage}
                disabled={currentPage === pages.length - 1 || isFlipping}
                className="book-btn"
                >
                    Siguiente →
                </button>
            </div>
        </div>
    );
};

export default BookComponent;