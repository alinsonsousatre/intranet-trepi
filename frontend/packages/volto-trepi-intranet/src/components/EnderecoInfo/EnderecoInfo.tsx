import React from 'react';
import { Container } from '@plone/components';
import type { Area } from 'volto-trepi-intranet/types/content';

interface EnderecoInfoProps {
  content: Area;
}

const EnderecoInfo: React.FC<EnderecoInfoProps> = ({ content }) => {
  const { endereco, complemento, cidade, estado, cep } = content;

  return (
    <Container narrow className="contato">
      <Container className="endereco">
        <span className="label">Endereço</span>:{' '}
        <span className="value">{endereco}</span>
      </Container>
      <Container className="complemento">
        <span className="label">Compleneto</span>:{' '}
        <span className="value">{complemento}</span>
      </Container>
      <Container className="cidade">
        <span className="label">cidade</span>:{' '}
        <span className="value">{cidade}</span>
      </Container>
      <Container className="estado">
        <span className="label">estado</span>:{' '}
        <span className="value">{estado}</span>
      </Container>
      <Container className="cep">
        <span className="label">cep</span>: <span className="value">{cep}</span>
      </Container>
    </Container>
  );
};

export default EnderecoInfo;
