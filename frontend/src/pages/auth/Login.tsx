// @flow
import React, { useState } from "react";
import { Button, Alert, Row, Col } from "react-bootstrap";
import { Auth } from "aws-amplify";
import * as yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import {
  Link,
  useNavigate,
  useLocation,
  createSearchParams,
} from "react-router-dom";
import { useTranslation } from "react-i18next";

import VerticalForm from "../../components/VerticalForm";
import FormInput from "../../components/FormInput";

import AccountLayout from "./AccountLayout";

/* bottom link of account pages */
const BottomLink = () => {
  const { t } = useTranslation();

  return (
    <Row className="mt-3">
      <Col className="text-center">
        <p className="text-muted">
          {t("Don't have an account?")}{" "}
          <Link to={"/sign-up"} className="text-muted ms-1">
            <b>{t("Sign Up")}</b>
          </Link>
        </p>
      </Col>
    </Row>
  );
};

const Login = () => {
  const { t } = useTranslation();
  let navigate = useNavigate();
  let location = useLocation();

  const [error, setError] = useState(null as string | null);
  const [loading, setLoading] = useState(false);

  let from = location.state?.from?.pathname || "/";

  function handleSubmit(value: { [key: string]: any }) {
    let email = value["username"] as string;
    let password = value["password"] as string;

    setLoading(true);
    Auth.signIn(email, password)
      .then(() => {
        // Send them back to the page they tried to visit when they were
        // redirected to the login page. Use { replace: true } so we don't create
        // another entry in the history stack for the login page.  This means that
        // when they get to the protected page and click the back button, they
        // won't end up back on the login page, which is also really nice for the
        // user experience.
        navigate(from, { replace: true });
      })
      .catch((reason: Error) => {
        setLoading(false);
        if (reason.name == "UserNotConfirmedException") {
          navigate(
            {
              pathname: "/enter-confirmation-code",
              search: `?${createSearchParams({ email })}`,
            },
            {
              state: { from: location.state?.from },
            }
          );
        } else {
          setError(reason.message);
        }
      });
  }

  /*
    form validation schema
    */
  const schemaResolver = yupResolver(
    yup.object().shape({
      username: yup.string().required(t("Please enter Username")),
      password: yup.string().required(t("Please enter Password")),
    })
  );

  return (
    <>
      <AccountLayout bottomLinks={<BottomLink />}>
        <div className="text-center w-75 m-auto">
          <h4 className="text-dark-50 text-center mt-0 fw-bold">
            {t("Sign In")}
          </h4>
          <p className="text-muted mb-4">
            {t(
              "Enter your email address and password to upload, process and manage data."
            )}
          </p>
        </div>

        {error && (
          <Alert variant="danger" className="my-2">
            {error}
          </Alert>
        )}

        <VerticalForm
          onSubmit={handleSubmit}
          resolver={schemaResolver}
          defaultValues={{ username: "", password: "" }}
        >
          <FormInput
            label={t("Username")}
            type="text"
            name="username"
            placeholder={t("Enter your Username")}
            containerClass={"mb-3"}
          />
          <FormInput
            label={t("Password")}
            type="password"
            name="password"
            placeholder={t("Enter your password")}
            containerClass={"mb-3"}
          >
            <Link to="/forgot-password" className="text-muted float-end">
              <small>{t("Forgot your password?")}</small>
            </Link>
          </FormInput>

          <div className="mb-3 mb-0 text-center">
            <Button variant="primary" type="submit" disabled={loading}>
              {t("Log In")}
            </Button>
          </div>
        </VerticalForm>
      </AccountLayout>
    </>
  );
};

export default Login;
