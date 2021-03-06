import React from 'react';
import { BtnContainer } from '../../styled-css';
import { Link } from 'react-router-dom';
import PayPalButton from './paypal-button';

export default function CartTotal({value, history}) {
    const {clearCart, cartSubTotal, cartTax, cartTotal} = value;
    return (
        <React.Fragment>
            <div className="container">
                <div className="row">
                    <div className="col-10 mt-2 ml-sm-5 ml-md-auto col-sm-8 text-right pull-right">
                        <Link to='/'>
                            <BtnContainer onClick={() => clearCart()} clearCart>clear cart</BtnContainer>
                        </Link>
                    </div>
                    <div className="col-10 mt-2 ml-sm-5 ml-md-auto col-sm-8 text-capitalize text-right">
                        <span style={{fontSize:'1.2rem'}}>cart subtotal : Rs. {cartSubTotal}</span>
                    </div>
                    <div className="col-10 mt-2 ml-sm-5 ml-md-auto col-sm-8 text-capitalize text-right">
                        <span style={{fontSize:'1.2rem'}}>total tax : Rs. {cartTax}</span>
                    </div>
                    <div className="col-10 mt-2 ml-sm-5 ml-md-auto col-sm-8 text-capitalize text-right">
                        <span style={{fontSize:'1.2rem'}}>total : Rs. {cartTotal}</span>
                    </div>
                    <div className="col-10 mt-2 ml-sm-5 ml-md-auto col-sm-8 text-capitalize text-right">
                        <PayPalButton totalAmt={cartTotal} clearCart={clearCart} history={history} />
                    </div>
                </div>
            </div>
        </React.Fragment>
    );
};