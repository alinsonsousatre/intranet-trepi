import type { Content, RelatedItem } from '@plone/types';

export interface Area extends Content {
  title: string;
  description: string;
  telefone?: string;
  email?: string;
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: {
    token: string;
    title?: string;
  };
  cep?: string;
  text?: {
    data: string;
    'content-type': string;
  };
}

export interface Pessoa extends Content {
  title: string;
  description: string;
  telefone?: string;
  email?: string;
  endereco?: string;
  complemento?: string;
  cidade?: string;
  estado?: {
    token: string;
    title: string;
  };
  cep?: string;
  cargo?: {
    token: string;
    title?: string;
  };
  token?: string;
  area?: RelatedItem;
}
